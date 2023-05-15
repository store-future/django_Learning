#here we handle request and respomce cycle for our web dev

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def  homepageview(request):
    return HttpResponse("Hello,world")