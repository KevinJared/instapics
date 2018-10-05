from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    CATEGORIES =(("Travel","Travel"),("Food","Food"),("Fashion","Fashion"),("Movies","Movies"))

    image_category = models.CharField(max_length=40,choices=CATEGORIES,)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,category,update):
        update = cls.objects.filter(image_category=category).update(image_category=update)
        return update


    def __str__(self):
        return self.image_category

class Location(models.Model):
    LOCATIONS=(("Kisumu","Kisumu"),("Mombasa","Mombasa"),("Nairobi","Nairobi"),("Eldoret","Eldoret"),)

    image_location = models.CharField(max_length=40,choices=LOCATIONS,)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,location,update):
        update = cls.objects.filter(image_location=location).update(image_location=update)
        return update


    def __str__(self):
        return self.image_location

class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='nothing')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_date = models.DateTimeField(auto_now_add=True)  
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.image_description
    def __unicode__(self):
        return self.category


    class Meta:
        ordering = ['image_name']
        #find out

    def save_image(self):
        self.save()


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    image = models.ImageField(upload_to='articles/', blank=True)
    tag = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news


    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
