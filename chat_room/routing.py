from channels.routing import route, include
from chat_room.consumers import ws_connect, ws_message, ws_disconnect, ws_qwe, ws_qwe_connect, ws_qwe_disconnect

channel_routing = [
    route("websocket.connect", ws_connect, path=r"^/room/(?P<room_id>\d+)/"),
    route("websocket.receive", ws_message, path=r"^/room/(?P<room_id>\d+)/"),
    route("websocket.disconnect", ws_disconnect, path=r"^/room/(?P<room_id>\d+)/"),
    route("websocket.connect", ws_qwe_connect, path=r"^/qwe/"),
    route("websocket.receive", ws_qwe, path=r"^/qwe/"),
    route("websocket.disconnect", ws_qwe_disconnect, path=r"^/qwe/"),
]
