from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^$',views.content_of_day,name='contentToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^new/article$', views.new_article, name='new-article'),
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)