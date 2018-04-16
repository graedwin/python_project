from __future__ import unicode_literals
from django.db import models
from ..login_and_registration.models import *

class Post(models.Model):
    pic=models.ImageField()
    posted_by=models.ForeignKey(Uer,related_name=posts)
    liked_by=models.ManyToManyField(User,related_name='likes')
