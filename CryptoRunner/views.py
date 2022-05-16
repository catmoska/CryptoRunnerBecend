from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import *
from hashlib import sha224
from datetime import datetime, timezone, timedelta
from .logik import *
import json


def mainStronisa(request):
    return render(request, 'CryptoRunner/mainStronisa.html', {'title': 'главная страниса'})


def pageNotFound(request, exception):
    return HttpResponseNotFound(Eroor404(request))


def Eroor404(request):
    return render(request, 'Eroor404.html', {'title': 'Error 404'})


def Razrabotka(request):
    return render(request, 'Razrabotka.html', {'title': 'Coming Soon!'})


def geimV(request):
    return render(request, 'CryptoRunner/Vgeimes.html', {'title': 'Geimes'})


@csrf_exempt
def MARKETPLACE(request):
    # users = Pleir.objects.filter(PublicKeuSolana="HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav")
    # if request.COOKIES:
    #     users = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
    #     if len(users) == 0:
    #         return nereadres("registr")
    # else:
    #     return nereadres("registr")

    MARKETPLACE = MARKETPLACEmodel.objects.all()
    return render(request, 'CryptoRunner/MARKETPLACE.html',
                  {'title': 'MARKETPLACE', "tovar": MARKETPLACE})


def MARKETPLACEI(request, geim):
    # return HttpResponse("hes  "+str(geim))
    return nereadres("main")


@csrf_exempt
def nftCilka(request, nftHeh):
    users = Pleir.objects.filter(PublicKeuSolana="HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav")
    # if request.COOKIES:
    #     users= Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
    #     if len(users) ==0:
    #         return nereadres("registr")
    # else:
    #     return nereadres("registr")
    user = users[0]

    nft = NFTs.objects.filter(idHash=nftHeh)
    if len(nft) == 0:
        return nereadres("Eroor404")
    nft = nft[0]

    if len(request.body) != 0:
        data = json.loads(request.body.decode('utf-8'))
        print(data["onerasia"])
        if data["onerasia"] == "bui":
            nft.Pleir = user
            nft.save()
            marc = MARKETPLACEmodel.objects.filter(nft=nft)
            marc.delete()
        elif data["onerasia"] == "sell":
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
    if user == nft.Pleir:
        pleir = True
    print(marxet)
    print(pleir)

    return render(request, 'CryptoRunner/NFT.html',
                  {'title': 'nft', "NFT": nft, "market": marxet, "pleir": pleir, "stoimost": stoimost})


@csrf_exempt
def registr(request):
    if request.COOKIES:
        snis = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
        if len(snis) != 0:
            return nereadres("geim")

    if len(request.body) != 0:
        PublicKeuSolana = json.loads(request.body.decode('utf-8'))["id"]
        snis = Pleir.objects.filter(PublicKeuSolana=PublicKeuSolana)
        idHash = sha224(PublicKeuSolana.encode('utf-8')).hexdigest()
        if len(snis) != 0:
            y = snis[0]
            y.DataVixada = datetime.now(timezone.utc)
            if request.COOKIES and request.COOKIES.get('id') != PublicKeuSolana:
                print("ddddd")
                y.isSiter = True
            y.save()
        else:
            y = Pleir(
                DataRegistr=datetime.today(),
                DataVixada=datetime.today(),
                PublicKeuSolana=PublicKeuSolana,
                idHash=idHash)
            y.save()
            nft = NFTs(
                Energia=3, EnergiaMax=3,
                idHash=str(random.randint(-100, 100)), DataSozdania=datetime.now(timezone.utc),
                DataVixada=datetime.now(timezone.utc),
                Pleir=y, СlothesTip=Сlothes.objects.all()[0])
            nft.save()
        response = redirect('/registr/')
        response.set_cookie('id', PublicKeuSolana)
        return response
        # return HttpResponse(y.SetIdHash())

    return render(request, 'CryptoRunner/registr.html', {'title': 'регистрасия'})


@csrf_exempt
def geimDETA(request):
    # userv = Pleir.objects.filter(PublicKeuSolana="HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav")
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
        if len(userv) == 0:
            return HttpResponse("registr")
    else:
        # return nereadres("registr")
        return HttpResponse("registr")
    userv = userv[0]

    if len(request.body) != 0:
        data = convert(request.body.decode('utf-8'))
        if data['Nonztia'] == "1":
            nft = NFTs.objects.filter(idHashPleir=userv.idHash)[int(data['NFTVID'])]
            nft.Energia += 1
            nft.DataVixada = datetime.now(timezone.utc)
            userv.Energia += 1
            nft.save()
            userv.save()
            return HttpResponse("")

        print(data)
        userv.Money += float(data['Money'])
        userv.Distansion += float(data['Distansion'])
        userv.Record = float(data['Distansion'])
        nft = NFTs.objects.filter(Pleir=userv)[int(data['NFTVID'])]
        if nft.Energia <= 0:
            print("EroorNFTEnergia")
            return HttpResponse("EroorNFTEnergia")
        if nft.Energia == nft.EnergiaMax:
            print("ddddddddddddddd")
            print(nft.DataVixada)
            nft.DataVixada = datetime.now(timezone.utc)
        nft.Energia -= 1
        userv.save()
        nft.save()
        deita(userv)
        print("es")
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


@csrf_exempt
def geim(request):
    if request.COOKIES:
        user = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
        if len(user) == 0:
            return nereadres("registr")
        nft = NFTs.objects.filter(Pleir=user[0])
        if len(nft) == 0:
            return nereadres("MARKETPLACE")
    else:
        return nereadres("registr")

    if len(request.body) != 0:
        print("dasssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

    return render(request, 'CryptoRunner/geim.html', {'title': 'geim'})
