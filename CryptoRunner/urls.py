from django.urls import path
from .views import *


urlpatterns = [
    path('', mainStronisa,name="main"),
    path('registr/', registr,name="registr"),

    path('games/cryptorunner', geim,name="geimCryptoRunner"),
    path('games/', geimV,name="Vgeim"),
    path('DATA/', geimDETA),
    path('marketplace/', MARKETPLACE,name="MARKETPLACE"),

    path('nft/', nftCilka, name="nft"),
    path('nft/<str:nftHeh>', nftCilka),

    path('profil/', profil),
]

urlpatterns+=[
    path('vistavka/', nftVistavka),
    path('E404/', Eroor404, name="Eroor404"),
    path('soonpage/', Razrabotka, name="Razrabotka"),
]
