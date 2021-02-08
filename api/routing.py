from django.urls import path

from .consumers import WSConsumer

websocket_urlpatterns = [
   path('ws/tasks/', WSConsumer.as_asgi()),
]