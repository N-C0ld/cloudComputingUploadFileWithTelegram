from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bucket(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class file(models.Model):
    bucket = models.ForeignKey(bucket, on_delete=models.CASCADE)
    route = models.TextField(max_length=max)
    type = models.TextField(max_length=50)