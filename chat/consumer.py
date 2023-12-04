from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async


def get_room_service():
    from chat.services.chat_room import ChatRoomService

    return ChatRoomService


class ChatRoomConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_service = None
        self.room_group_name = None
        self.user = None
        self.room_id = None
        self.room = None

    async def connect(self):
        print('WebSocket connection established.')

        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.user = self.scope["user"]
        self.room_service = get_room_service()
        self.room = await self.room_service.a_get_by_id(self.room_id)
        self.room_group_name = f'chat_{self.room_id}'

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        await self.room_service.join_room(obj_id=self.room_id, user=self.user)

        await self.send_message({"content": f"{self.user.username} joined"})

    async def disconnect(self, close_code):
        await self.leave_room()

        print('late==>')
        # Remove the custom event handler upon disconnect
        await self.channel_layer.group_discard(f"chat_{self.room_id}", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if not text_data:
            return

        request = json.loads(text_data)
        data = request.get("data")
        action = data.get("action")
        if not action:
            return
        if action == "send_message":
            await self.send_message(request.get("data"))
        if action == "leave_room":
            await self.leave_room()

    async def leave_room(self):
        # Retrieve necessary data from the event

        # Call the leave_room method from ChatRoomService or perform necessary actions
        await self.room_service.leave_room(obj_id=self.room_id, user=self.user)

        await self.send_message({"content": f"{self.user.username} left the room"})
        # Disconnect the user from the WebSocket
        await self.close()  # This disconnects the user from the WebSocket

    async def send_message(self, message):
        # Send message to WebSocket
        from .services.message import MessageService

        res = await MessageService.log_message(self.room, self.user, message)
        print('sending message===>', res)
        await self.send(text_data=res)
