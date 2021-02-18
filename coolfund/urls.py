
from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_genres),


    path('api', views.getuseripinfo),
]