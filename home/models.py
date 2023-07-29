from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    subtitle = models.CharField(max_length=255,blank=True,null=True)
    hero_image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

class SocialPlatform(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    facebook_link = models.CharField(max_length=255,blank=True,null=True)
    twitter_link = models.CharField(max_length=255,blank=True,null=True)
    instagram_link = models.CharField(max_length=255,blank=True,null=True)
    tiktok_link = models.CharField(max_length=255,blank=True,null=True)
    threads_link = models.CharField(max_length=255,blank=True,null=True)

class Client(models.Model):
    name =  models.CharField(max_length=100,null=True,)
    logo = models.ImageField(upload_to="client_logo/")
    website = models.URLField(blank=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class TeamMember(models.Model):
    name = models.CharField(max_length=255,null=True)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    
    def __str__(self):
        return self.name



class Message(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=False, null=False )
    message = models.TextField()
    subject = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name