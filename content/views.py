from django.http  import HttpResponse
from django.shortcuts import render
import datetime as dt
from .models import Image, Location, Category

# Create your views here.
def content_of_day(request):
    all_images = Image.objects.all()
    return render(request, 'all-images/content.html', {"images": all_images})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def get_location(request,location):
    image = Image.filter_location(location)
    return render(request,'location.html',locals())

def get_category(request,category):
    image = Image.filter_category(category)
    return render(request,'category.html',locals())

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})

def content(request,image_id):
    try:
        content = Content.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/article.html", {"content":content})(request, 'all-images/search.html',{"message":message})