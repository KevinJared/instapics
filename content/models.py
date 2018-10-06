from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="profile/a.jpg")
    bio = models.TextField(max_length=50, blank=True)


class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(max_length=50 , blank=True)
    post_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    liker = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE,null=True)

class Comment(models.Model):
    message = models.TextField(max_length=50)
    user = models.ForeignKey(User, related_name='commented_by', on_delete=models.CASCADE)
    image = models.ForeignKey(Post, related_name='comment_for', on_delete=models.CASCADE)
