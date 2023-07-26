from django.shortcuts import render
from .models import Hero,SocialPlatform,Client,TeamMember
# Create your views here.
def display_page(request):
    my_hero = Hero.objects.first()  # it gets the first object/item in the Hero table and this will return none if hero object doesnt exits
    social_platform = SocialPlatform.objects.last()
    clients = Client.objects.filter(display=True)
    team_members = TeamMember.objects.all()
    if not my_hero:
        my_hero =  Hero.objects.create(title="Hero title",subtitle="Hero Subtitle") # if not exist we create a new object
    context ={
        'social_platform':social_platform,
        'title':my_hero.title,
        'subtitle':my_hero.subtitle,
        'hero_image':my_hero.hero_image,
        'clients':clients,
        'team_members':team_members,
    
    }
    return render(request,'index.html',context)