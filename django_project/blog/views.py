from django.shortcuts import render
from django.http import HttpResponse
from .models import  Post

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return  render(request,"blog/home.html",context)
    # view should always return a http response or an exception
    # render does that in the background

# Create your views here.


def about(request):
    return render(request,"blog/about.html", {"title":"About"})