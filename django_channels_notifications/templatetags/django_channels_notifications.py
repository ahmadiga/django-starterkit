from django import template
from django.template import loader

from django_channels_notifications.models import Notification

register = template.Library()


@register.simple_tag(takes_context=True)
def render_notifications_drawer(context):
    request = context['request']
    if request.user.is_authenticated:
        csrf_token = context['csrf_token']
        user = request.user
        notifications = Notification.objects.filter(to_user=user)

        # load html template
        template_path = "django_channels_notifications/notifications_drawer.html"
        t = loader.get_template(template_path)
        # prepare context
        context = {
            'request': request,
            "notifications": notifications
        }
        # load file upload foorm if inline form setting is True
        html = t.render(context)
        return html
    else:
        return ""
