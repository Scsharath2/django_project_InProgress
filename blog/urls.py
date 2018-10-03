from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name = 'blog_home'),#(redirect to homepage,function we created in views.py,view name)
    path('about/', views.About,name = 'blog_about'),
]
