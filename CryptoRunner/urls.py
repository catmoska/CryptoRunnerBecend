from django.urls import path
from .views import *


urlpatterns = [
    path('', mainStronisa,name="main"),
    path('registr/', registr,name="registr"),
    # path('profil/', profil,name="profil"),
    # path('profilN/', profiln,name="profilN"),
    # path('geim/DATA/', geimDETA),

    path('Gaim', geim,name="geim"),
    path('Geimes', geimV,name="Vgeim"),
    path('DATA/', geimDETA),
    path('E404', Eroor404,name="Eroor404"),
    path('Razrabotka', Razrabotka,name="Razrabotka"),
    path('MARKETPLACE', MARKETPLACE,name="MARKETPLACE"),
    path('MARKETPLACE/<int:geim>', MARKETPLACEI,name="MARKETPLACEiii"),
]