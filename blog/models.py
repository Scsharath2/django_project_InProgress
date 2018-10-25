from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_lenght=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default.timezone)
    author = models.Foreignkey(User,onDelete=models.CASCADE)
