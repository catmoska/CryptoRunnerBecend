from django.urls import path
from .views import *


urlpatterns = [
    path('', mainStronisa,name="main"),
    # path('registr/', registr,name="registr"),
    # path('profil/', profil,name="profil"),
    # path('profilN/', profiln,name="profilN"),
    path('Gaim', geim,name="geim"),
    # path('geim/DATA/', geimDETA),
    path('DATA/', geimDETA),
]