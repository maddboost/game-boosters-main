from django.urls import path ,re_path
from chat.consumers import ChatConsumer


websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_slug>[^/]+)/$', ChatConsumer.as_asgi()),
]