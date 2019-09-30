from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.random_generator),
    url(r'^reset$', views.reset),


]
