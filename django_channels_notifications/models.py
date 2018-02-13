from __future__ import unicode_literals
# Create your models here.
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class UserChannels(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    html = models.CharField(max_length=255)


class Notification(models.Model):
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='from_user', null=True, blank=True, on_delete=models.CASCADE)
    html = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)

    def send_notification(self):
        user_group = "notification-" + str(self.to_user_id)
        user_notifications = Notification.objects.filter(to_user=self.to_user).order_by("-created_date")
        if user_notifications.count() > 100:
            for i in range(100, user_notifications.count()):
                user_notifications[i].delete()

        count_unread = Notification.objects.filter(to_user=self.to_user, is_read=False).count()

        # Group(user_group).send(
        #     {'text': json.dumps({'notifications': [notification_data, ], 'count_unread': count_unread,
        #                          'show_notifications': True, })})

    def save(self, *args, **kwargs):
        is_insert = not self.pk
        super(Notification, self).save(*args, **kwargs)
        if is_insert:
            self.send_notification()

    def __str__(self):
        return self.text
