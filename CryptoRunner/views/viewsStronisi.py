from .logik import *

#########Eroor страниси
def Eroor404_E(request,Error):
    return render(request, 'Eroor404.html', {'title': 'Error 404',"stronisa":True,"Eroor":Error})

# @cache_page(60 * 60)
def Eroor404_(request):
    return render(request, 'Eroor404.html', {'title': 'Error 404',"stronisa":True,"Eroor":""})

#######################

# главная страниса
# @cache_page(60 * 60)
def mainStronisa_(request):
    return render(request, 'CryptoRunner/mainStronisa.html', {'title': 'главная страниса',"stronisa":True})


# страниса показа игор
# @cache_page(60 * 60)
def geimStranisa_(request):
    return render(request, 'CryptoRunner/Vgeimes.html', {'title': 'Geimes',"stronisa":True})


# страниса разработки
# @cache_page(60 * 60)
def Razrabotka_(request):
    return render(request, 'Razrabotka.html', {'title': 'Coming Soon!',"stronisa":True})

