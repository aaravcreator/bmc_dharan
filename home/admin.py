from django.contrib import admin
from .models import Hero,SocialPlatform,Client,TeamMember
# Register your models here.
admin.site.register(Hero)
admin.site.register(SocialPlatform)
admin.site.register(Client)
admin.site.register(TeamMember)