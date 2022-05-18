from django.http import HttpResponseRedirect
from .models import *
# from hashlib import sha224
from datetime import datetime, timezone,timedelta
# import datetime
import json
import random
times = timedelta(minutes=81)

def nereadres(urls):
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


    # isklusenia2 = []
    # if naram == 1:
    #     for i in isklusenia:
    #         isklusenia2.append(i.skin)
    # if naram == 2:
    #     for i in isklusenia:
    #         isklusenia2.append(i.suit)
    # if naram == 3:
    #     for i in isklusenia:
    #         isklusenia2.append(i.trousers)
    # if naram == 4:
    #     for i in isklusenia:
    #         isklusenia2.append(i.cap)
    # if naram == 5:
    #     for i in isklusenia:
    #         isklusenia2.append(i.gloves)
    #
    # isklusenia = np.array(isklusenia2)
    # del isklusenia2
    # i = 0
    # while True:
    #     i+=1
    #     sislo = random.randint(min,max)
    #     t = isklusenia[isklusenia==sislo]
    #     if len(t) == 0:
    #         return sislo


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



