"""
ASGI config for djangoChatServer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumer import ChatRoomConsumer
from core.channel_middleware import ChannelJWTAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoChatServer.settings')
django_asgi_app = get_asgi_application()


websocket_urlpatterns = [
    path('ws/chat_room/<int:room_id>/', ChatRoomConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': ChannelJWTAuthMiddleware(  # Add your middleware here in the stack
        URLRouter(websocket_urlpatterns)
    ),
})
