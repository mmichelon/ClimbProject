from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (http->django views is added by default)
})

# from channels.routing import route
#
# channel_routing = [
#     route('websocket.receive', 'chat.consumers.ws_echo'),
#     # route('websocket.connect', 'chat.consumers.ws_add'),
# ]
