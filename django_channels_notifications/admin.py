# Register your models here.
from django.contrib import admin

from django_channels_notifications.models import Notification

admin.site.register(Notification)
