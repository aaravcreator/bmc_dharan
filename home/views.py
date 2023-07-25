from django.shortcuts import render
from .models import Hero
# Create your views here.
def display_page(request):
    my_hero = Hero.objects.first()  # it gets the first object/item in the Hero table and this will return none if hero object doesnt exits
    if not my_hero:
        my_hero =  Hero.objects.create(title="Hero title",subtitle="Hero Subtitle") # if not exist we create a new object
    context ={
        # 'title':"Welcome to BMC DHARAN",
        'title':my_hero.title,
        'subtitle':my_hero.subtitle,
        # 'sub_title':"One of the leading IT College in Dharan",
        'mydata': [
            "football",
            "volleyball",
            "basketball"
        ]
    }
    return render(request,'index.html',context)