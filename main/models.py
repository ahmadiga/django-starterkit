from __future__ import unicode_literals
from django.db.models import Model, CharField


class Survey(Model):
    name = CharField(max_length=100)
    phone = CharField(max_length=20)
    email = CharField(max_length=50)
