from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author":"Satya",
        "title":"Blog post ",
        "content":"First Post content",
        "date_posted":"August 27,2018"
    },
    {
        "author": "Dileep",
        "title": "Blog post 2",
        "content": "First Post content",
        "date_posted": "August 27,2018"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return  render(request,"blog/home.html",context)
    # view should always return a http response or an exception
    # render does that in the background

# Create your views here.


def about(request):
    return render(request,"blog/about.html", {"title":"About"})