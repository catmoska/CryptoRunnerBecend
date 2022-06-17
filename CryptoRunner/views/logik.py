from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, \
    JsonResponse, HttpResponsePermanentRedirect
import random
import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha224

# from .DateTimeF import *
# from bs4 import BeautifulSoup
# import requests as req
# import solana
# from solana.transaction import *

import CryptoRunnerBecend.settings
from django.views.decorators.cache import cache_page
from CryptoRunner.forms import *
from CryptoRunner.models import *
from .config import *



# замена print()
def printF(p):
    if CryptoRunnerBecend.settings.DEBUG:
        print(p)


# создает HttpResponse с изменениям силки
def nereadres(urls,eror = "",request=None):
    if urls == "Eroor404":
        if request!=None and request.method == 'GET':
            JsonResponse({"Eroor": True})
        raise Http404(eror)
    url = reverse(urls)
    response = HttpResponseRedirect(url)
    return response


# конвертируе
def convert(nojson):
    jsons = '{"'
    for i in nojson:
        if i != "&" and i != "=":
            jsons+=i
        elif i == "&":
            jsons+='","'
        elif i == "=":
            jsons+='":"'
    jsons+='"}'
    return json.loads(jsons)


#  поиск nft (яблуко = зелоная)
def NoiskNft(nftArrau,Heh):
    for i in range(len(nftArrau)):
        if nftArrau[i].idHash == Heh:
            return i
    return None


# (в разработке) провераяет пришовшую сигнатуру на доставерность
def nroverkaSignatura(signatura):
    printF("signatura")
    # r = TransactionSignature
    # printF(r)


# рандом для BOX
def resULTATBokTip(BokTip):
    if random.randint(0, int(100 / BokTip[0])):
        return 0
    elif random.randint(0,int(100/BokTip[1])):
        return 1
    elif random.randint(0, int(100 / BokTip[2])):
        return 2
    elif random.randint(0,int(100/BokTip[3])):
        return 3
    return 3


# рандом для BOX N количество
def resULTATBokTipX(BokTip):
    for i in range(len(BokTip)):
        if random.randint(0, int(100 / BokTip[i])):
            return i
    return len(BokTip)-1


# обновления енергий у всех nft у играка
def deita(user: Pleir):
    NFTSS = NFTs.objects.filter(Pleir=user)
    for nft in NFTSS:
        if nft.Energia != nft.EnergiaMax:
            timesVremina = datetime_now_F() - nft.DataVixada
            nft.Energia += int(timesVremina / times)
            nft.DataVixada += int(timesVremina / times) * times
            if nft.Energia > nft.EnergiaMax:
                nft.Energia = nft.EnergiaMax
                nft.DataVixada = datetime_now_F()
        else:
            nft.DataVixada = datetime_now_F()
        nft.save()


# обновления енергий у одного nft
def deitaNFT(nft: NFTs):
    if nft.Energia != nft.EnergiaMax:
        timesVremina = datetime_now_F() - nft.DataVixada
        nft.Energia += int(timesVremina / times)
        nft.DataVixada += int(timesVremina / times) * times
        if nft.Energia > nft.EnergiaMax:
            nft.Energia = nft.EnergiaMax
            nft.DataVixada = datetime_now_F()
    else:
        nft.DataVixada = datetime_now_F()
    nft.save()


# создания nft
def sozdaniaNft(pleir,Tip,y=True):
    time = datetime_now_F()

    kolisestvo = len(NFTs.objects.all())
    kolisestvoCloat = len(Сlothes.objects.all())

    if kolisestvoCloat == 0:
        printF("EroorСlothes одезду добав")
        return HttpResponse("EroorСlothes")
    elif kolisestvoCloat > 1:
        cloat = Сlothes.objects.all()[random.randint(0, kolisestvoCloat - 1)]
    else:
        cloat = Сlothes.objects.all()[0]

    hes = (str(time) + str(random.randint(-100, 100))) * random.randint(1, 3)
    idHash = sha224(hes.encode('utf-8')).hexdigest()
    Energia = EnergiaSpisok[Tip]

    nft = NFTs(
        Nick="Bonny NFT#" + str(kolisestvo + 1),
        Energia=Energia, EnergiaMax=Energia,
        idHash=idHash, DataSozdania=time,
        DataVixada=time,
        Pleir=pleir, ClothesTip=cloat, Ymnozitel=Ymnozitel[Tip])
    nft.save()
    print(nft)
    if y:
        return nft
    return nft, idHash, cloat


# создания nft через Box
def sozdaniaNftBox(pleir,Box):
    time = datetime_now_F()

    kolisestvo = len(NFTs.objects.all())
    kolisestvoCloat = len(Сlothes.objects.all())

    if kolisestvoCloat == 0:
        printF("EroorСlothes одезду добав")
        return HttpResponse("EroorСlothes")
    elif kolisestvoCloat > 1:
        cloat = Сlothes.objects.all()[random.randint(0, kolisestvoCloat - 1)]
    else:
        cloat = Сlothes.objects.all()[0]

    tip = resULTATBokTip([Box.tip1, Box.tip2, Box.tip3, Box.tip4])

    hes = (str(time) + str(random.randint(-100, 100))) * random.randint(1, 3)
    idHash = sha224(hes.encode('utf-8')).hexdigest()
    Energia = EnergiaSpisok[tip]

    nft = NFTs(
        Nick="Bonny NFT#" + str(kolisestvo + 1),
        Energia=Energia, EnergiaMax=Energia,
        idHash=idHash, DataSozdania=time,
        DataVixada=time,
        Pleir=pleir, ClothesTip=cloat, Ymnozitel=Ymnozitel[tip])
    nft.save()

    return nft, idHash, cloat, tip


# генирирует полний списак даних для саитов
def siteDeta(title,user,stronisa,svoi=None):
    d1= {'title': title,"Referral":user.pk,"stronisa":stronisa}
    if svoi!=None:
        d1.update(svoi)
    return d1


