from channels.generic.websocket import AsyncWebsocketConsumer
import json


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

    async def connect(self):
        print('WebSocket connection established.')  # Use logger instead of print

        print(self.scope)
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.user = self.scope.get("user")
        self.room_group_name = f'chat_{self.room_id}'
        self.room_service = get_room_service()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        self.room_service.join_room(self.room_id, user=self.room_service.get_by_id(self.user.id))

    async def disconnect(self, close_code):
        # Leave room group when WebSocket is closed
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        self.room_service.leave_room(self.room_id, user=self.room_service.get_by_id(self.user.id))

    async def receive(self, text_data=None, bytes_data=None):
        if not text_data:
            return

        message = json.loads(text_data)
        # Example of handling a received message - you can modify this based on your application logic
        user = self.room_service.get_by_id(self.user.id)
        await self.send_message(f"{message}")
        self.room_service.send_message(self.room_id, user=user, message=f"{user.username}: {message}")

    async def send_message(self, message):
        # Send message to WebSocket

        await self.send(text_data=json.dumps({'message': message}))
