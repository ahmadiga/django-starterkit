from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.utils.log import get_task_logger

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

app = Celery('django_starterkit')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

logger = get_task_logger(__name__)


@app.task
def test():
    logger.info("test task")
