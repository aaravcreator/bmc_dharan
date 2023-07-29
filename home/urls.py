from django.urls import path
from .views import *


app_name = 'home'

urlpatterns = [
    path('',display_page,name="index"),
    path('send_message',handle_form,name="send_message"),
]