from django.urls import path
from .views import *


urlpatterns = [
    path('', mainStronisa_,name="main"),
    path('registr/', registr_,name="registr"),

    path('games/cryptorunner', geim_,name="geimCryptoRunner"),
    path('games/', geimStranisa_,name="Vgeim"),
    path('DATA/', geimDETA_),
    path('marketplace/', MARKETPLACE_,name="MARKETPLACE"),

    path('nft/', nftCilka_, name="nft"),
    path('nft/<str:nftHeh>', nftCilka_),

    path('profile/', profile_, name="profile"),
    path('profile/<str:profil>', profileX_),

    # path('Box/<str:N>', sunduk_),
]


urlpatterns+=[
    path('Referral/<str:referalni>', referalni_),
    path('vistavka/', nftVistavka_),
    path('E404/', Eroor404_, name="Eroor404"),
    path('soonpage/', Razrabotka_, name="Razrabotka"),
]
