from django.shortcuts import HttpResponse,render


def index(request):
    return HttpResponse("THIS IS A RESPONSE")


def display_name(request,name):
    return HttpResponse('Your name is {}'.format(name))


def display_page(request):
    context ={
        'title':"Welcome to BMC DHARAN",
        'sub_title':"One of the leading IT College in Dharan",
        'mydata': [
            "football",
            "volleyball",
            "basketball"
        ]
    }
    return render(request,'index.html',context)