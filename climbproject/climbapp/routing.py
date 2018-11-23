# from django.conf.urls import url, re_path, path
from django.urls import path, re_path

from . import consumers

# from .consumers import ChatConsumer

websocket_urlpatterns = [
    # path('ws/chat/<room_name>/', consumers.ChatConsumer),
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),

]
