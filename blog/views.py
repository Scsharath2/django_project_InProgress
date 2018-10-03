from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
      'author' : 'Sharath',
      'title' : 'Blog Post1',
      'content' :'First post content',
      'date_posted':'Oct 1,2018',
    },
    {
      'author' : 'Chandra',
      'title' : 'Blog Post2',
      'content' :'Second post content',
      'date_posted':'Oct 2,2018',
    }
]

# Create your views here.
def Home(request):
    context = {
    'posts' : posts
    }
    return render(request,'blog/home.html',context)

def About(request):
    return render(request,'blog/about.html',{'title':'About'})
