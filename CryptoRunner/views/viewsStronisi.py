from .logik import *

#########Eroor страниси
def Eroor404_E(request,Error):
    return render(request, 'Eroor404.html', {'title': Eroor404_neim,"stronisa":True,"Eroor":Error})

# @cache_page(60 * 60)
def Eroor404_(request):
    return render(request, 'Eroor404.html', {'title': Eroor404_neim,"stronisa":True,"Eroor":""})

#######################

# главная страниса
# @cache_page(60 * 60)
def mainStronisa_(request):
    return render(request, 'CryptoRunner/mainStronisa.html', {'title': mainStronisa_neim,"stronisa":True})


# страниса показа игор
# @cache_page(60 * 60)
def geimStranisa_(request):
    return render(request, 'CryptoRunner/Vgeimes.html', {'title': geimStranisa_neim,"stronisa":True})


# страниса разработки
# @cache_page(60 * 60)
def Razrabotka_(request):
    return render(request, 'Razrabotka.html', {'title': Razrabotka_neim, "stronisa":True})

