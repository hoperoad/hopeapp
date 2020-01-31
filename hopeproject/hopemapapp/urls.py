from django.urls import path

from . import views

app_name = 'hopemapapp'
urlpatterns = [
    path('', views.index),
]