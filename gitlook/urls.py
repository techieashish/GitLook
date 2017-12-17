__author__ = 'techieashish'
from django.conf.urls import url
from . import views

app_name = "glook"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^some$', views.some_view, name='some'),
]

