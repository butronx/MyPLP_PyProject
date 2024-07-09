from django.db import models

# Create your models here.
class Url(models.Model):
    link  = models.CharField(max_length=20000)
    uuid = models.CharField(max_length=12)