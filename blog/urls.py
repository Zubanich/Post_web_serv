from django.urls import path
from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'), 
    url(r'^author/(?P<author_name>\w+)/', views.author, name='author'),
    url(r'^formpost/$', views.formpost, name='formpost'), 
    url(r'^createpost/$', views.createpost, name='createpost'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]