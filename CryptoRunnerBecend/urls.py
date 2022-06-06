from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from CryptoRunner.views import *

urlpatterns = [
    path('', include("CryptoRunner.urls")),
    path('admin/', admin.site.urls),

]

handler404 = pageNotFound_

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += path('__debug__/', include('debug_toolbar.urls'))
