from channels.routing import route
from chat.consumers import ws_message, connect_chathome, http_consumer,disconnect_chathome

# The channel routing defines what channels get handled by what consumers,
# including optional matching on message attributes. WebSocket messages of all
# types have a 'path' attribute, so we're using that to route the socket.
# While this is under stream/ compared to the HTML page, we could have it on the
# same URL if we wanted; Daphne separates by protocol as it negotiates with a browser.


channel_routing = [
    # route("http.request", "chat.consumers.http_consumer"),
    route("websocket.receive", ws_message),
    route("websocket.connect", connect_chathome, path=r'^/stream/$'),
    route("websocket.disconnect", disconnect_chathome, path=r'^/stream/$'),
]


# A default "http.request" route is always inserted by Django at the end of the routing list
# that routes all unmatched HTTP requests to the Django view system. If you want lower-level
# HTTP handling - e.g. long-polling - you can do it here and route by path, and let the rest
# fall through to normal views.
