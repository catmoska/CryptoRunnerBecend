from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, \
    JsonResponse, HttpResponsePermanentRedirect
import random
import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha224

import CryptoRunnerBecend.settings
from .DateTimeF import *
from django.views.decorators.cache import cache_page
from CryptoRunner.forms import *
from CryptoRunner.models import *
from .config import *

# from bs4 import BeautifulSoup
# import requests as req
# import solana
# from solana.transaction import *


def printF(p):
    if CryptoRunnerBecend.settings.DEBUG:
        print(p)


def nereadres(urls):
    if urls == "Eroor404":
        raise Http404("")
    url = reverse(urls)
    response = HttpResponseRedirect(url)
    return response


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


def NoiskNft(nftArrau,Heh):
    for i in range(len(nftArrau)):
        if nftArrau[i].idHash == Heh:
            return i
    return None



def nroverkaSignatura(signatura):
    printF("signatura")
    # r = TransactionSignature
    # printF(r)



def nftCilkaPOST(data,nft,user):
    printF(data["onerasia"])
    if data["onerasia"] == "bui":
        #######################################
        # printF(data)
        # nroverka(data["signatura"])
        # printF("das")
        #######################################
        nft.Pleir = user
        nft.save()
        marc = MARKETPLACEmodel.objects.filter(nft=nft)
        marc.delete()
    elif data["onerasia"] == "sell":
        marc = MARKETPLACEmodel.objects.filter(nft=nft)
        if len(marc) == 0:
            R = MARKETPLACEmodel(nft=nft, stoimost=round(float(data["prise"]), 5))
            R.save()
    elif data["onerasia"] == "take off":
        marc = MARKETPLACEmodel.objects.filter(nft=nft)
        marc.delete()
    return HttpResponse("")



def resULTATBokTip(BokTip):
    resO = -1
    while True:
        random100 = random.randint(1, 99)
        res = 0
        q = 0
        for i in BokTip:
            if random100 > res:
                res += i
                q += 1
            elif random100 < res:
                resO = q

            if resO != -1:
                break
        if resO != -1:
            break
    return resO


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


def sozdaniaNft(pleir,Tip):
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
    return nft,idHash,cloat


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