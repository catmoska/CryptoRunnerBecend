from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from CryptoRunner.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("CryptoRunner.urls")),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
