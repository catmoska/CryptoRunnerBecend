from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404,\
    JsonResponse,HttpResponsePermanentRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from hashlib import sha224
from datetime import datetime, timezone, timedelta
from django.views.decorators.cache import cache_page
from .forms import *
from .logik import *
import json

# @cache_page(60 * 60)
def mainStronisa(request):
    return render(request, 'CryptoRunner/mainStronisa.html', {'title': 'главная страниса'})

# @cache_page(60 * 60)
def pageNotFound(request, exception):
    return HttpResponseNotFound(Eroor404(request))

# @cache_page(60 * 60)
def Eroor404(request):
    return render(request, 'Eroor404.html', {'title': 'Error 404'})


# @cache_page(60 * 60)
def Razrabotka(request):
    return render(request, 'Razrabotka.html', {'title': 'Coming Soon!'})


# @cache_page(60 * 60)
def geimV(request):
    return render(request, 'CryptoRunner/Vgeimes.html', {'title': 'Geimes'})


def profile(request):
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


def profile(request,profil):
    userv = Pleir.objects.filter(PublicKeuSolana=profil)
    if len(userv) == 0:
        return nereadres("Eroor404")
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
            registor = False
    else:
        registor = False

    nft = NFTs.objects.filter(idHash=nftHeh)
    if len(nft) == 0:
        return nereadres("Eroor404")
    nft = nft[0]
    deitaNFT(nft)

    if request.method == 'GETPARAMS':
        MARKETPLACE = MARKETPLACEmodel.objects.filter(nft=nft)
        if len(MARKETPLACE) == 0:
            return HttpResponse("ErorEczemplar")
        MARKETPLACE = MARKETPLACE[0]

        return JsonResponse(
            {"stoimost":MARKETPLACE.stoimost,
            "publickeusol":MARKETPLACE.nft.Pleir.PublicKeuSolana})

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        return nftCilkaPOST(data,nft,user)

    marxet = False
    pleir = False
    stoimost = 0
    marc = MARKETPLACEmodel.objects.filter(nft=nft)

    if len(marc) != 0:
        marxet = True
        stoimost = marc[0].stoimost

    if registor:
        user = users[0]
        if user == nft.Pleir:
            pleir = True

    response = render(request, 'CryptoRunner/NFT.html',
    {'title': 'nft', "NFT": nft, "market": marxet,
     "pleir": pleir, "stoimost": stoimost,"registor":registor})

    response.set_cookie('NFThistori', nftHeh)

    return response


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
            moneu =0
            if request.COOKIES:
                referal = request.COOKIES.get('referalnaiSika')
                if referal!=null:
                    snis = Pleir.objects.filter(pk=referal)
                    if len(snis) != 0:
                        snis = snis[0]
                        snis.Money += 100
                        snis.save()
                        moneu += 50

            y = Pleir(
                DataRegistr=datetime.today(),
                DataVixada=datetime.today(),
                PublicKeuSolana=PublicKeuSolana,
                idHash=idHash,Energia=20,EnergiaMax=20, Money=moneu)
            y.save()
            # nft = NFTs(
            #     Energia=3, EnergiaMax=3,
            #     idHash=str(random.randint(-100, 100)), DataSozdania=datetime.now(timezone.utc),
            #     DataVixada=datetime.now(timezone.utc),
            #     Pleir=y, СlothesTip=Сlothes.objects.all()[0])
            # nft.save()
        response = redirect('/registr/')
        response.set_cookie('publicKey', PublicKeuSolana)
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
    hehNFT = None
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(userv) == 0:
            return HttpResponse("TestPleir")
        hehNFT = request.COOKIES.get('NFThistori')
    else:
        return HttpResponse("TestPleir")
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

    otvet = str(userv.Money) + "&" + str(userv.Record) + "&" + str(userv.nonitka) + "$"


    if hehNFT !=None:
        i = NoiskNft(nft, Heh)
        if i !=None:
            nft[0],nft[i]=nft[i],nft[0]


    for i in nft:
        otvet += str(i.Energia) + "&" + str(i.EnergiaMax) + "&" + str(i.Nick) + "&" + \
                 str(0 if (i.Energia == i.EnergiaMax) else int(
                     (times - (datetime.now(timezone.utc) - i.DataVixada)).seconds / 60)) + "&" + \
                 str(i.ClothesTip.pk) + "$"

    if userv.nonitka:
        userv.nonitka = False
        userv.save()
    return HttpResponse(otvet)


def geim(request):
    if request.COOKIES:
        if request.COOKIES.get('publicKey') == None:
            return nereadres("registr")
        user = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(user) == 0:
            return nereadres("registr")
        if len(user) != 0:
            nft = NFTs.objects.filter(Pleir=user[0])
            # if len(nft) == 0:
            #     return nereadres("MARKETPLACE")
    else:
        return nereadres("registr")

    resultat = render(request, 'CryptoRunner/geim.html', {'title': 'geim'})
    # resultat.get_session_cookie_age("ddd","")
    return resultat



def referalni(request, referalni):
    response = redirect('/')
    response.set_cookie('referalnaiSika', referalni)
    return response


