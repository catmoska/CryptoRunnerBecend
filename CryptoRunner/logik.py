from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, \
    JsonResponse, HttpResponsePermanentRedirect

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha224
# from datetime import datetime, timezone, timedelta
from django.views.decorators.cache import cache_page
from .forms import *
from .models import *
from .logicDateTime import deita,deitaNFT,times
import random
import json
# from bs4 import BeautifulSoup
# import requests as req
# import solana
# from solana.transaction import *

EnergiaSpisok =[3,5,7,9]
Ymnozitel = [1, 1.5, 2, 3]
Glava = "AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw"



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


