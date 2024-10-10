from django.db import models
from django.db.models import *


class User(models.Model):
    name = CharField(max_length=15, null=False)
    surname = CharField(max_length=20, null=False)
    age = IntegerField(max_length=3, null=True),
    email = CharField(max_length=60, null=False),
    address = CharField(max_length=50, null=True)

