from django.urls import path
from .consumers import ChessConsumer

websocket_urlpatterns = [
    path("ws/chess/", ChessConsumer.as_asgi()),
]
