from django.shortcuts import render
from . import models
import requests, uuid, json
from django.http import HttpResponse, JsonResponse
# Create your views here.
def show_genres(request):
    return render(request, "cool.html", {'genres': models.Genre.objects.all()})


def getuseripinfo(request):

    return render(request, 'ip/index.html', locals())


def postuserposition(request):
    data = {}
    return JsonResponse(data, safe=False)


def trackopenmail(request):
    
    image_data ="https://nanspace.s3.amazonaws.com/businessstatic/ressources/images/logo-nan.png"
    response = requests.get(image_data)

    return HttpResponse(response.content, content_type="image/png")