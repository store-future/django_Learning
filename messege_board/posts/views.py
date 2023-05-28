from django.shortcuts import render

# Create your views here.

# listview= it return us a context variable (modelname_list) and context means that can change or who hold the result of sth

from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    template_name="home.html"
    model = Post
    