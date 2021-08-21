from django.db import models

# Create your models here.
class Tweet(models.Model):
    username = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    datetime = models.DateTimeField(auto_now_add=True)