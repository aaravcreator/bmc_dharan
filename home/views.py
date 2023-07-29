from django.shortcuts import render,redirect
from .models import Hero,SocialPlatform,Client,TeamMember,Message
from django.core.mail import EmailMessage
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


def handle_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        
        mero_message = Message.objects.create(name=name,email=email,message=message,subject=subject)
        body = "Message set by  {}\n {}".format(mero_message.name,mero_message.message)
        mero_email = EmailMessage(subject=mero_message.subject,body=body,from_email='poudelaarav@gmail.com',to=['075bei001@ioepc.edu.np'])
        mero_email.send()
        return redirect('home:index')