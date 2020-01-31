from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from hopemapapp.models import HopeEmployee
import googlemaps
import requests

MY_API_KEY = "AIzaSyAgUMk7cdxV7kM3CuOpILllYnvVxV7hbK8"
URL_FORMAT = "https://maps.googleapis.com/maps/api/staticmap?center={}"\
    "&zoom={}&size={}&format={}{}&maptype=roadmap"\
    "&key={}"

def index(request):
    all_hopeEmployees = HopeEmployee.objects.all()
   # for hopeEmployee in all_hopeEmployees:

    template = loader.get_template('index.html')
    context = {
        'all_hopeEmployees':all_hopeEmployees
    }
    return HttpResponse(template.render(context, request))
