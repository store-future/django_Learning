
#i made this url.py file to accept data from view and generate a proper 
#url link which is connected to our project url link

from django.urls import path
from .views import homepageview


urlpatterns = [
    path("",homepageview,name="home")  #generating a url for homepageview
]