from __future__ import unicode_literals
from django.db import models
from ..login_and_registration.models import *

class Post(models.Model):
    pic=models.ImageField()
    posted_by=models.ForeignKey(User,related_name='posts')
    liked_by=models.ManyToManyField(User,related_name='likes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content=models.TextField()
    commented_by=models.ForeignKey(User,related_name='comments')
    post=models.ForeignKey(Post,related_name='comments')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
