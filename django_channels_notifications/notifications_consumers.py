# In consumers.py
import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger('django.channels')


class NotificationsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            user_group = "notification-" + str(self.user.id)
            self.channel_layer.group_add(user_group, self.channel_name)
            logger.info(vars(self))
            logger.info(async_to_sync(self.channel_name))
            # self.prepare_notifications()
            # Called on connection. Either call
            await self.accept()
            await self.send(text_data="Hello world!")
        else:
            # Or to reject the connection, call
            await self.close()

    async def prepare_notifications(self):
        pass
        # user_group = "notification-" + str(user.id)
        # Group(user_group).add(self.reply_channel)
        # notifications = Notification.objects.filter(to_user=user).order_by("-created_date")[:6]
        # count_unread = Notification.objects.filter(to_user=user, is_read=False).count()
        # Group(user_group).send({'text': json.dumps(
        #     {
        #         # 'notifications': notifications,
        #         'count_unread': count_unread, 'show_notifications': False, })})

    async def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        await self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        await self.send(bytes_data=b"Hello world!")
        # Want to force-close the connection? Call:
        # await self.close()
        # # Or add a custom WebSocket error code!
        # await self.close(code=4123)

    async def disconnect(self, close_code):
        self.user = self.scope["user"]
        user_group = "notification-" + str(self.user.id)
        self.channel_layer.group_discard(user_group, self.channel_name)
        await self.close()

# @channel_session_user_from_http
# def notifications_ws_add(message):
#     # Add them to the right group
#     if message.user.is_authenticated:
#         user = message.user
#         prepare_notifications(message, user)
#
#
# # Connected to websocket.disconnect
# @channel_session_user
# def notifications_ws_disconnect(message):
#     if message.user.is_authenticated:
#         user = message.user
#         user_group = "notification-" + str(user.id)
#         Group(user_group).discard(message.reply_channel)
