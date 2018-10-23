from django.db import models

# Create your models here.
class ClimbModel(models.Model):
    climb = models.CharField(max_length=240)

    def __str__(self):
        return climb
