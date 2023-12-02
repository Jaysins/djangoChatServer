from ninja import Router
from typing import List

from .serializers import ChatRoomInputSchema, ChatRoomResponseSchema
from .services.chat_room import ChatRoomService

router = Router()


@router.post("/chat_rooms/", response=ChatRoomResponseSchema)
def signup(request, req_data: ChatRoomInputSchema):
    req_data = req_data.model_dump()
    req_data['user'] = request.user_context.get("user_id")
    # Create the user
    return ChatRoomService.create(**req_data)


@router.get("/chat_rooms/", response=List[ChatRoomResponseSchema])
def signup(request):
    # Create the user
    user = request.user
    all_rooms = ChatRoomService.filter(user=user.get("id"))

    return all_rooms
