from django.shortcuts import render
from geopy.geocoders import Nominatim

# Create your views here.

def home(request):
    data = {
        'countrycode':'fr',
    }
    return render(request, 'index.html', data)


def result(request):
    if request.method == 'POST':
        lieu = request.POST.get('location')
        geolocator = Nominatim(user_agent="test")
        location = geolocator.geocode(lieu)
        print(location)

        data = {
            'long': location.longitude,
            'lat': location.latitude,
            'add': location.address
        }

    return render(request, 'result.html', data)