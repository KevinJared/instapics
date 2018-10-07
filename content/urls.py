from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(?P<user_id>\d+)?$', views.profile, name='profile'),
    url(r'follow/(?P<user_id>\d+)', views.follow, name='follow'),
    url(r'^update/profile$', views.updateprofile, name='updateprofile'),
    url(r'^comment/(?P<post_id>\d+)$', views.comment_on, name='comment'),
    url(r'^search/(?P<name>.+)$', views.find, name='save'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)