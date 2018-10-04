from django.db import models
import datetime as dt
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
        return self.image_name
    def __unicode__(self):
        return self.category


    class Meta:
        ordering = ['image_name']
        #find out

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__image_category__icontains=search_term)
        return gallery

    @classmethod
    def filter_location(cls,location):
        # location = Location.objects.(image_location=location)
        images = cls.objects.filter(location__image_location__istartswith=location)
        return images
    @classmethod
    
    def filter_category(cls,category):
        images = cls.objects.filter(category__image_category__istartswith=category)
        return images
