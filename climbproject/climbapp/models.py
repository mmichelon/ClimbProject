from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClimbModel(models.Model):
    climb = models.CharField(max_length=240)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return self.climb
        return "%s authored by %s" % (self.climb,self.author)
