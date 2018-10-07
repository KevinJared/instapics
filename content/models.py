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
    bio = models.TextField(max_length=500, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()

    def comment(self, photo, text):
        Comment(text=text, photo=photo, user=self).save()

class Post(models.Model):
    image = models.FileField(upload_to='posts/')
    caption = models.TextField(max_length=50 , blank=True)
    post_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    liker = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE,null=True)

    @property
    def get_comments(self):
        return self.comments.all()

    class Meta:
        ordering = ["-pk"]

class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(Profile, related_name='comments')
