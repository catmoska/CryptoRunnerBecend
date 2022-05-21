from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from hashlib import sha224
from datetime import datetime, timezone, timedelta
from django.views.decorators.cache import cache_page
from .forms import *
from .logik import *
import json

# @cache_page(60 * 60 * 10)
def mainStronisa(request):
    return render(request, 'CryptoRunner/mainStronisa.html', {'title': 'главная страниса'})


def pageNotFound(request, exception):
    return HttpResponseNotFound(Eroor404(request))


def Eroor404(request):
    return render(request, 'Eroor404.html', {'title': 'Error 404'})


# @cache_page(60 * 60*10)
def Razrabotka(request):
    return render(request, 'Razrabotka.html', {'title': 'Coming Soon!'})


# @cache_page(60 * 60)
def geimV(request):
    return render(request, 'CryptoRunner/Vgeimes.html', {'title': 'Geimes'})


def profil(request):
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(userv) == 0:
            return nereadres("registr")
    else:
        return nereadres("registr")
    user = userv[0]

    NFT = NFTs.objects.filter(Pleir = user)
    NFTCOl = len(NFT)

    return render(request, 'CryptoRunner/profil.html',
                  {'title': 'profil', "tovar": NFT,"user":user,"NFTCOl":NFTCOl})


@csrf_exempt
def MARKETPLACE(request):
    MARKETPLACE = MARKETPLACEmodel.objects.all()
    return render(request, 'CryptoRunner/MARKETPLACE.html',
                  {'title': 'MARKETPLACE', "tovar": MARKETPLACE})


@csrf_exempt
def nftCilka(request, nftHeh):
    registor =True
    if request.COOKIES:
        users = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(users) ==0:
            if request.method == 'GET':
                registor = False
            else:
                return nereadres("registr")
    else:
        if request.method == 'GET':
            registor = False
        else:
            return nereadres("registr")
    if registor:
        user = users[0]

    nft = NFTs.objects.filter(idHash=nftHeh)
    if len(nft) == 0:
        return nereadres("Eroor404")
    nft = nft[0]

    if request.method == 'GETPARAMS':
        MARKETPLACE = MARKETPLACEmodel.objects.filter(nft=nft)
        if len(MARKETPLACE) == 0:
            return HttpResponse("ErorEczemplar")
        MARKETPLACE = MARKETPLACE[0]
        jso = {"stoimost":MARKETPLACE.stoimost,
               "publickeusol":MARKETPLACE.nft.Pleir.PublicKeuSolana}
        return JsonResponse(jso)
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data["onerasia"])
        if data["onerasia"] == "bui":
            #######################################
            print(data)
            nroverka(data["signatura"])
            print("das")
            #######################################
            nft.Pleir = user
            nft.save()
            marc = MARKETPLACEmodel.objects.filter(nft=nft)
            marc.delete()
        elif data["onerasia"] == "sell":
            marc = MARKETPLACEmodel.objects.filter(nft=nft)
            if len(marc)==0:
                R = MARKETPLACEmodel(nft=nft, stoimost=0.05)
                R.save()
        elif data["onerasia"] == "take off":
            marc = MARKETPLACEmodel.objects.filter(nft=nft)
            marc.delete()
        return HttpResponse("")

    marxet = False
    pleir = False
    stoimost = 0
    marc = MARKETPLACEmodel.objects.filter(nft=nft)
    if len(marc) != 0:
        marxet = True
        stoimost = marc[0].stoimost
    if registor:
        if user == nft.Pleir:
            pleir = True

    return render(request, 'CryptoRunner/NFT.html',
                  {'title': 'nft', "NFT": nft, "market": marxet, "pleir": pleir, "stoimost": stoimost,"registor":registor})


@csrf_exempt
def registr(request):
    if request.COOKIES:
        snis = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(snis) != 0:
            return nereadres("geimCryptoRunner")

    if request.method == 'POST':
        PublicKeuSolana = json.loads(request.body.decode('utf-8'))["publicKey"]
        snis = Pleir.objects.filter(PublicKeuSolana=PublicKeuSolana)
        idHash = sha224(PublicKeuSolana.encode('utf-8')).hexdigest()
        if len(snis) != 0:
            y = snis[0]
            y.DataVixada = datetime.now(timezone.utc)
            y.save()
        else:
            y = Pleir(
                DataRegistr=datetime.today(),
                DataVixada=datetime.today(),
                PublicKeuSolana=PublicKeuSolana,
                idHash=idHash,Energia=20,EnergiaMax=20)
            y.save()
            # nft = NFTs(
            #     Energia=3, EnergiaMax=3,
            #     idHash=str(random.randint(-100, 100)), DataSozdania=datetime.now(timezone.utc),
            #     DataVixada=datetime.now(timezone.utc),
            #     Pleir=y, СlothesTip=Сlothes.objects.all()[0])
            # nft.save()
        response = redirect('/registr/')
        response.set_cookie('publicKey', PublicKeuSolana)
        print("das")
        return response

    return render(request, 'CryptoRunner/registr.html', {'title': 'регистрасия'})


def nftVistavka(request):
    ppublic = ["HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav",
               "871FK4JkgGDsQB7nDwgcTPJ8KR1ErE9nHd6L8cXQFopY",
               "AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw"]
    if request.COOKIES:
        users = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(users) == 0:
            return nereadres("registr")
        y =False
        for i in ppublic:
            if request.COOKIES.get('publicKey') == i:
                y = True
                pass
        if not y:
            return nereadres("main")
    else:
        return nereadres("main")

    if request.method == 'POST':
        form = NewForms(request.POST)
        pleir = Pleir.objects.filter(PublicKeuSolana="AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw")[0]
        if form.is_valid():
            colisestvo = form.cleaned_data["colisestvo"]
            stoimostStart = form.cleaned_data["stoimostStart"]
            Neriod = form.cleaned_data["Neriod"]
            startSislo = form.cleaned_data["startSislo"]

            for i in range(colisestvo):
                cloat = Сlothes.objects.all()[random.randint(0,1)]
                print(cloat)
                hes = (str(datetime.now(timezone.utc))+str(random.randint(-100, 100)))*random.randint(1, 3)
                idHash = sha224(hes.encode('utf-8')).hexdigest()
                nft = NFTs(
                    Nick="Bonny NFT#"+str(i+1+startSislo),
                    Energia=3, EnergiaMax=3,
                    idHash=idHash, DataSozdania=datetime.now(timezone.utc),
                    DataVixada=datetime.now(timezone.utc),
                    Pleir=pleir,ClothesTip=cloat)
                nft.save()
                R = MARKETPLACEmodel(nft=nft, stoimost=round((stoimostStart+Neriod*i),5))
                R.save()
        return nereadres("MARKETPLACE")
    elif request.method == 'GET':
        form = NewForms()
        return render(request, 'CryptoRunner/nftVistavka.html', {"form":form})
    return HttpResponse("Eroor")


@csrf_exempt
def geimDETA(request):
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(userv) == 0:
            return HttpResponse("registr")
    else:
        return HttpResponse("registr")
    userv = userv[0]

    if request.method == 'POST':
        data = convert(request.body.decode('utf-8'))
        if data['Nonztia'] == "1":
            nft = NFTs.objects.filter(idHashPleir=userv.idHash)[int(data['NFTVID'])]
            nft.Energia += 1
            nft.DataVixada = datetime.now(timezone.utc)
            userv.Energia += 1
            nft.save()
            userv.save()
            return HttpResponse("")

        userv.Money += float(data['Money'])
        userv.Distansion += float(data['Distansion'])
        userv.Record = float(data['Distansion'])
        nft = NFTs.objects.filter(Pleir=userv)[int(data['NFTVID'])]
        if nft.Energia <= 0:
            print("EroorNFTEnergia")
            return HttpResponse("EroorNFTEnergia")
        if nft.Energia == nft.EnergiaMax:
            nft.DataVixada = datetime.now(timezone.utc)
        nft.Energia -= 1
        userv.save()
        nft.save()
        deita(userv)
        return HttpResponse("")

    deita(userv)
    nft = NFTs.objects.filter(Pleir=userv)
    if len(nft) == 0:
        return HttpResponse("EroorNFT")

    otvet:str = str(userv.Money) + "&" + str(userv.Record) + "&" + str(userv.nonitka) + "$"

    for i in nft:
        otvet += str(i.Energia) + "&" + str(i.EnergiaMax) + "&" + str(i.Nick) + "&" + \
                 str(0 if (i.Energia == i.EnergiaMax) else int(
                     (times - (datetime.now(timezone.utc) - i.DataVixada)).seconds / 60)) + "&" + \
                 str(i.ClothesTip.pk) + "$"

    if userv.nonitka:
        userv.nonitka = False
        userv.save()
    return HttpResponse(otvet)


# @csrf_exempt
def geim(request):
    if request.COOKIES:
        user = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(user) == 0:
            return nereadres("registr")
        nft = NFTs.objects.filter(Pleir=user[0])
        if len(nft) == 0:
            return nereadres("MARKETPLACE")
    else:
        return nereadres("registr")


    return render(request, 'CryptoRunner/geim.html', {'title': 'geim'})
