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

    path('profile/', profile, name="profile"),
    path('profile/<str:profil>', profileZ),

    path('sunduk/<str:N>', sunduk ),
]


urlpatterns+=[
    path('Referral/<str:referalni>', referalni),
    path('vistavka/', nftVistavka),
    path('E404/', Eroor404, name="Eroor404"),
    path('soonpage/', Razrabotka, name="Razrabotka"),
]
