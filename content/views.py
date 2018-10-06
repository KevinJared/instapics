from django.http  import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NewArticleForm
import datetime as dt
from .models import Image, Likes, Comments
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/') 
def content_of_day(request):
    all_images = Image.objects.all()
    return render(request, 'all-images/content.html', {"images": all_images})

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'all-images/profile.html', {"profile": profile})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def content(request,image_id):
    try:
        content = Content.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/article.html", {"content":content})(request, 'all-images/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('contentToday')

    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})