from django.shortcuts import render
from . import models
# Create your views here.
def show_genres(request):
    return render(request, "cool.html", {'genres': models.Genre.objects.all()})


def getuseripinfo(request):


    return render(request, 'ip/index.html', locals())