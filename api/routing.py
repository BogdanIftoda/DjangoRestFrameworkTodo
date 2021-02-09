from django.urls import path

from .consumers import NotificationConsumer

websocket_urlpatterns = [
   path('ws/tasks/', NotificationConsumer.as_asgi()),
]