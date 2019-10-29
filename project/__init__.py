"""
Celery ...
"""
from __future__ import absolute_import, unicode_literals
import os
import django

from .celery import app as celery_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

__all__ = ['celery_app']
