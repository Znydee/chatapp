# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<room>/<username>/', consumers.ChatConsumer.as_asgi()),
]