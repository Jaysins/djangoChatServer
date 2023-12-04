from ninja import Router
from djangoChatServer.exceptions import CustomValidationError
from .serializers import *
from .services.chat_room import ChatRoomService

router = Router()


@router.get("/chat_rooms/", response=List[ChatRoomResponseSchema])
def get_all_chat_room(request):
    return ChatRoomService.filter(user=request.user)


@router.get("/chat_rooms/{room_id}", response=ChatRoomResponseSchema)
def get_single_chat_room(request, room_id: str):
    return ChatRoomService.get_by_id(room_id)


@router.get("/chat_rooms/{room_id}/participants", response=List[UserResponseSchema])
def get_chat_room_participants(request, room_id: str):
    return ChatRoomService.get_room_participants(int(room_id))


@router.get("/open_chat_rooms/", response=List[ChatRoomResponseSchema])
def get_open_chat_room(request):
    return ChatRoomService.filter(is_private=False)


@router.get("/joined_chat_rooms", response=List[ChatRoomResponseSchema])
def get_joined_chat_room(request):
    return ChatRoomService.filter(participants=request.user)


@router.post("/chat_rooms/", response=ChatRoomResponseSchema)
def create_chat_room(request, req_data: ChatRoomInputSchema):
    return ChatRoomService.create(user=request.user, **req_data.model_dump())


@router.post("/chat_rooms/{room_id}", response=ChatRoomResponseSchema)
def update_chat_room(request, room_id: str, req_data: ChatRoomUpdateSchema):
    room = ChatRoomService.get_by_id(obj_id=room_id)

    if not room:
        raise CustomValidationError(message="Requested resource does not exist")

    if room.user.id != request.user.id:
        raise CustomValidationError(message="You do not have access to this resource")

    req_data = req_data.model_dump()
    validated_data = {key: value for key, value in req_data.items() if value is not None}

    if not validated_data:
        return room

    return ChatRoomService.update(int(room_id), **validated_data)


@router.post("/chat_rooms/{room_id}/join", response=ChatRoomResponseSchema)
def join_chat_room(request, room_id: str, req_data: JoinChatRoomInputSchema):
    req_data = req_data.model_dump()
    req_data['user'] = request.user
    room = ChatRoomService.get_by_id(obj_id=room_id)

    if not room:
        raise CustomValidationError(message="Requested resource does not exist")

    if room.max_participants is not None and room.participants.count() >= room.max_participants:
        raise CustomValidationError(message="Room full")

    return ChatRoomService.join_room(int(room_id), **req_data)


@router.post("/chat_rooms/{room_id}/leave", response=DefaultResponseSchema)
def leave_chat_room(request, room_id: str, req_data: JoinChatRoomInputSchema):
    req_data = req_data.model_dump()
    req_data['user'] = request.user
    room = ChatRoomService.get_by_id(obj_id=room_id)

    if not room:
        raise CustomValidationError(message="Requested resource does not exist")

    return ChatRoomService.leave_room(int(room_id), **req_data)
