from django.urls import path
from .views import *


urlpatterns = [
    path('', mainStronisa,name="main"),
    path('registr/', registr,name="registr"),
    # path('profil/', profil,name="profil"),
    # path('profilN/', profiln,name="profilN"),
    # path('geim/DATA/', geimDETA),

    path('games/cryptorunner', geim,name="geim"),
    path('games/', geimV,name="Vgeim"),
    path('DATA/', geimDETA),
    path('E404/', Eroor404,name="Eroor404"),
    path('soonpage/', Razrabotka,name="Razrabotka"),
    path('marketplace/', MARKETPLACE,name="MARKETPLACE"),

    path('nft/', nftCilka,name="nft"),
    path('nft/<str:nftHeh>', nftCilka,name="nft"),
    path('marketplace/<int:geim>', MARKETPLACEI),
]