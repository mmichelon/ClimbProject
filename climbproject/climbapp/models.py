from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class ClimbModel(models.Model):
    climb = models.CharField(max_length=240)
    difficulty = models.CharField(max_length=10)

    outdoor_bool = models.BooleanField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.climb

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    climb = models.ForeignKey(ClimbModel, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s authored by %s" % (self.climb,self.author)

# Real time chat System
