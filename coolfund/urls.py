
from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_genres),


    path('api', views.getuseripinfo),
    path('img', views.trackopenmail),
    path('post', views.postuserposition),
]