from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/',default='nothing')
    bio = models.TextField()

    def save_category(self):
        self.save()


class Likes(models.Model):
    image_likes = models.CharField(max_length=40)

    def save_category(self):
        self.save()

class Comments(models.Model):
    image_comments = models.TextField(max_length=40)

    def save_location(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='nothing')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    likes = models.CharField(max_length=40)
    comments = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_caption

    def __unicode__(self):
        return self.category


    class Meta:
        ordering = ['image_name']
        #find out

    def save_image(self):
        self.save()
        
class Article(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    @classmethod
    def search_by_image(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
