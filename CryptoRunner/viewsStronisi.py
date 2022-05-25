from .logik import *

# @cache_page(60 * 60)
def Eroor404(request):
    return render(request, 'Eroor404.html', {'title': 'Error 404',"stronisa":True})


# @cache_page(60 * 60)
def mainStronisa(request):
    return render(request, 'CryptoRunner/mainStronisa.html', {'title': 'главная страниса',"stronisa":True})


# @cache_page(60 * 60)
def geimV(request):
    return render(request, 'CryptoRunner/Vgeimes.html', {'title': 'Geimes',"stronisa":True})


# @cache_page(60 * 60)
def Razrabotka(request):
    return render(request, 'Razrabotka.html', {'title': 'Coming Soon!',"stronisa":True})

