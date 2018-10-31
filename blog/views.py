from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse


# Create your views here.
def Home(request):
    context = {
    'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def About(request):
    return render(request,'blog/about.html',{'title':'About'})
