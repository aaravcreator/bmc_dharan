from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    subtitle = models.CharField(max_length=255,blank=True,null=True)
    