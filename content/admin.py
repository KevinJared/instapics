from django.contrib import admin
from .models import Image, Likes, Comments

admin.site.register(Image)
admin.site.register(Likes)
admin.site.register(Comments)