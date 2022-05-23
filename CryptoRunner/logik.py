from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, \
    JsonResponse, HttpResponsePermanentRedirect

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha224
from datetime import datetime, timezone, timedelta
from django.views.decorators.cache import cache_page
from .forms import *
from .models import *
import random
import json
# from bs4 import BeautifulSoup
# import requests as req
# import solana
# from solana.transaction import *



times = timedelta(minutes=81)

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


def genirator():
    parametris = {
        "skin": randomIsklusenia(0,len(Сlothes.objects.filter(Narameter=1)),1),
        "suit": randomIsklusenia(0,len(Сlothes.objects.filter(Narameter=2)),2),
        "trousers": randomIsklusenia(0,len(Сlothes.objects.filter(Narameter=3)),3),
        "cap": randomIsklusenia(0,len(Сlothes.objects.filter(Narameter=4)),4),
        "gloves": randomIsklusenia(0,len(Сlothes.objects.filter(Narameter=5)),5),
    }
    return parametris


def randomIsklusenia(min,max,naram):
    i=0
    if naram == 1:
        while True:
            i += 1
            sislo = random.randint(min, max)
            t = NFTs.objects.filter(skin=sislo)
            if len(t) == 0:
                return sislo
    if naram == 2:
        while True:
            i+=1
            sislo = random.randint(min,max)
            t = NFTs.objects.filter(suit=sislo)
            if len(t) == 0:
                return sislo
    if naram == 3:
        while True:
            i+=1
            sislo = random.randint(min,max)
            t = NFTs.objects.filter(trousers=sislo)
            if len(t) == 0:
                return sislo
    if naram == 4:
        while True:
            i+=1
            sislo = random.randint(min,max)
            t = NFTs.objects.filter(cap=sislo)
            if len(t) == 0:
                return sislo
    if naram == 5:
        while True:
            i+=1
            sislo = random.randint(min,max)
            t = NFTs.objects.filter(gloves=sislo)
            if len(t) == 0:
                return sislo


def deita(user:Pleir):
    NFTSS = NFTs.objects.filter(Pleir=user)
    for nft in NFTSS:
        if nft.Energia != nft.EnergiaMax:
            timesVremina = datetime.now(timezone.utc) - nft.DataVixada
            nft.Energia += int(timesVremina / times)
            nft.DataVixada += int(timesVremina / times)*times
            if nft.Energia > nft.EnergiaMax:
                nft.Energia = nft.EnergiaMax
                nft.DataVixada = datetime.now(timezone.utc)
        else:
            nft.DataVixada = datetime.now(timezone.utc)
        nft.save()

def deitaNFT(nft:NFTs):
    if nft.Energia != nft.EnergiaMax:
        timesVremina = datetime.now(timezone.utc) - nft.DataVixada
        nft.Energia += int(timesVremina / times)
        nft.DataVixada += int(timesVremina / times)*times
        if nft.Energia > nft.EnergiaMax:
            nft.Energia = nft.EnergiaMax
            nft.DataVixada = datetime.now(timezone.utc)
    else:
        nft.DataVixada = datetime.now(timezone.utc)
    nft.save()


def NoiskNft(nftArrau,Heh):
    for i in range(len(nftArrau)):
        if nftArrau[i].idHash == Heh:
            return i
    return None



def nroverka(signatura):
    print("signatura")



    # r = TransactionSignature
    # print(r)



def nftCilkaPOST(data,nft,user):
    print(data["onerasia"])
    if data["onerasia"] == "bui":
        #######################################
        # print(data)
        # nroverka(data["signatura"])
        # print("das")
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






