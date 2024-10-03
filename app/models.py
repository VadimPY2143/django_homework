from django.db import models
from django.db.models import *

class User(models.Model):
    name = CharField(max_length=15, null=False)
    surname = CharField(max_length=20, null=False)
    age = IntegerField(null=False),
    email = EmailField(null=False),
    address = CharField(max_length=50, null=True)

