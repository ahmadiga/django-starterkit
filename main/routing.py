from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#
# channel_routing = [
#     route("websocket.connect", notifications_ws_add, path=r"^/ws/django_channels_notifications/$"),
#     route("websocket.disconnect", notifications_ws_disconnect, path=r"^/ws/django_channels_notifications/$"),
# ]
from django.conf.urls import url

from django_channels_notifications.notifications_consumers import NotificationsConsumer

application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url("^ws/django_channels_notifications/$", NotificationsConsumer),
        ])
    ),

})
