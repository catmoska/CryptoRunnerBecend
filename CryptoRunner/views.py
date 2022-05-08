from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect , HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import *
from hashlib import sha224
from datetime import datetime, timezone,timedelta
from .logik import *
import json

def pageNotFound(request,exception):
    return HttpResponseNotFound(Eroor404(request))

def Eroor404(request):
    return render(request, 'Eroor404.html', {'title': 'Error 404'})

def Razrabotka(request):
    return render(request, 'Razrabotka.html', {'title': 'Coming Soon!'})

def geimV(request):
    return render(request, 'CryptoRunner/Vgeimes.html', {'title': 'Geimes'})

def MARKETPLACE(request):
    return render(request, 'CryptoRunner/MARKETPLACE.html', {'title': 'MARKETPLACE',"tovar":[0,1,2,3,4,5,6,7,8,9,10]})

def MARKETPLACEI(request,geim):
    if(geim == 1):
        return render(request, 'CryptoRunner/MARKETPLACE.html',
                      {'title': 'MARKETPLACE', "tovar": [0, 1, 2]})
    return render(request, 'CryptoRunner/MARKETPLACE.html', {'title': 'MARKETPLACE',"tovar":[0,1,2,3,4,5]})




def mainStronisa(request):
    return render(request, 'CryptoRunner/mainStronisa.html', {'title':'главная страниса'})


# @csrf_exempt
# def registr(request):
#     if request.COOKIES:
#         snis = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
#         if len(snis) !=0:
#             return nereadres("geim")
#
#     if len(request.body) !=0:
#         PublicKeuSolana= json.loads(request.body.decode('utf-8'))["id"]
#         snis = Pleir.objects.filter(PublicKeuSolana=PublicKeuSolana)
#         idHash = sha224(PublicKeuSolana.encode('utf-8')).hexdigest()
#         print(idHash)
#         print(PublicKeuSolana)
#         if len(snis) !=0:
#             y = snis[0]
#             y.DataVixada = datetime.now()
#             if request.COOKIES and request.COOKIES.get('id') != PublicKeuSolana:
#                 print("ddddd")
#                 y.isSiter = True
#             y.save()
#         else:
#             y = Pleir(
#             DataRegistr=datetime.today(),
#             DataVixada=datetime.today(),
#             Energia=20,
#             EnergiaMax=20,
#             PublicKeuSolana=PublicKeuSolana,
#             idHash=idHash)
#             y.save()
#             nft = NFTs(
#                 Energia=3,EnergiaMax=3,
#                 idHash="",URLnft='',
#                 Obrabotka=True,DataSozdania=datetime.now(),
#                 DataVixada=datetime.now(),Narameter={'id': "dd"},
#                 idHashPleir=y.idHash,skin=0, suit=0, trousers=0,
#                 cap=0, gloves=0)
#             nft.save()
#         response = redirect('/registr/')
#         response.set_cookie('id',PublicKeuSolana)
#         return response
#         # return HttpResponse(y.SetIdHash())
#
#     return render(request,'CryptoRunner/registr.html', {'title':'регистрасия'})



@csrf_exempt
def geimDETA(request):
    # userv = Pleir.objects.filter(PublicKeuSolana="HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav")
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
        if len(userv) ==0:
            return HttpResponse("registr")
    else:
        # return nereadres("registr")
        return HttpResponse("registr")
    userv = userv[0]

    if len(request.body) != 0:
        data = convert(request.body.decode('utf-8'))
        if data['Nonztia'] =="1":
            nft = NFTs.objects.filter(idHashPleir=userv.idHash)[int(data['NFTVID'])]
            nft.Energia += 1
            userv.Energia += 1
            nft.save()
            userv.save()
            return HttpResponse("")

        userv.Money+= float(data['Money'])
        userv.Distansion += float(data['Distansion'])
        userv.Record = float(data['Distansion'])
        userv.Energia -= 1
        nft = NFTs.objects.filter(idHashPleir=userv.idHash)[int(data['NFTVID'])]
        if userv.Energia <= 0:
            return HttpResponse("EroorPleirEnergia")
        if nft.Energia <= 0:
            return HttpResponse("EroorNFTEnergia")
        if nft.Energia == nft.EnergiaMax:
            nft.DataVixada == datetime.now(timezone.utc)
        nft.Energia -= 1
        userv.save()
        nft.save()
        return HttpResponse("")

    deita(userv)
    nft = NFTs.objects.filter(idHashPleir=userv.idHash)
    if len(nft) == 0:
        return HttpResponse("EroorNFT")


    otvet =str(userv.Money)+"&"+str(userv.Record)+"&"+\
           str(userv.Energia)+"&"+str(userv.EnergiaMax)+"&"+str(userv.nonitka)+"$"

    for i in nft:
        otvet+=str(i.Energia)+"&"+str(i.EnergiaMax)+"&"+str(i.Nick)+"&"+\
               str(i.skin)+"&"+str(i.suit)+"&"+str(i.trousers)+"&"+str(i.cap)+\
               "&"+str(i.gloves)+"&"+\
               str(0 if (i.Energia == i.EnergiaMax)else int((times-(datetime.now(timezone.utc) - i.DataVixada)).seconds/60))+"$"

    if userv.nonitka:
        userv.nonitka = False
        userv.save()
    return HttpResponse(otvet)

@csrf_exempt
def geim(request):
    # if request.COOKIES:
    #     user = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('id'))
    #     if len(user) ==0:
    #         return nereadres("registr")
    # else:
    #     return nereadres("registr")

    if len(request.body) !=0:
        PublicKeuSolana= json.loads(request.body.decode('utf-8'))["id"]
        snis = Pleir.objects.filter(PublicKeuSolana=PublicKeuSolana)
        idHash = sha224(PublicKeuSolana.encode('utf-8')).hexdigest()
        print(idHash)
        print(PublicKeuSolana)
        if len(snis) !=0:
            y = snis[0]
            y.DataVixada = datetime.now()
            if request.COOKIES and request.COOKIES.get('id') != PublicKeuSolana:
                y.isSiter = True
            y.save()
        else:
            y = Pleir(
            DataRegistr=datetime.today(),
            DataVixada=datetime.today(),
            Energia=20,
            EnergiaMax=20,
            PublicKeuSolana=PublicKeuSolana,
            idHash=idHash)
            y.save()
            nft = NFTs(
                Energia=3,EnergiaMax=3,
                idHash="",URLnft='',
                Obrabotka=True,DataSozdania=datetime.now(),
                DataVixada=datetime.now(),Narameter={'id': "dd"},
                idHashPleir=y.idHash,skin=0, suit=0, trousers=0,
                cap=0, gloves=0)
            nft.save()
        response = redirect('/')
        response.set_cookie('id',PublicKeuSolana)
        return response
        # return HttpResponse(y.SetIdHash())

    return render(request,'CryptoRunner/geim.html', {'title':'geim'})










