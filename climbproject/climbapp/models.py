from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClimbModel(models.Model):
    climb = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return self.climb
        return "%s authored by %s" % (self.climb,self.author)

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    climb = models.ForeignKey(ClimbModel, on_delete=models.CASCADE)

    def __str__(self):
        return "%s authored by %s" % (self.climb,self.author)
