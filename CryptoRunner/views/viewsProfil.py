from .logik import *

########## страниса
@csrf_exempt
def registr_(request):
    if request.COOKIES:
        snis = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(snis) != 0:
            return nereadres("geimCryptoRunner")

    if request.method == 'POST':
        return registr_POST(request)
    elif request.method == 'GET':
        return render(request, 'CryptoRunner/registr.html', {'title': registr_neim})
    else:
        printF("Eroor: registr_: request.method !=")
        return HttpResponse("Eroor")


def registr_POST(request):
    PublicKeuSolana = json.loads(request.body.decode('utf-8'))["publicKey"]
    snis = Pleir.objects.filter(PublicKeuSolana=PublicKeuSolana)
    idHash = sha224(PublicKeuSolana.encode('utf-8')).hexdigest()

    if len(snis) != 0:
        y = snis[0]
        y.DataVixada = datetime_now_F()
        y.save()
    else:
        moneu = 0
        if request.COOKIES:
            referal = request.COOKIES.get('referalnaiSika')
            if referal != None:
                snis = Pleir.objects.filter(pk=referal)
                if len(snis) != 0:
                    snis = snis[0]
                    snis.Money += 100
                    snis.save()
                    moneu += 50

        y = Pleir(
            Nick=PublicKeuSolana,
            DataRegistr=datetime_today(),
            DataVixada=datetime_today(),
            PublicKeuSolana=PublicKeuSolana,
            idHash=idHash, Money=moneu)
        y.save()

        # sozdaniaNft(y,1)

    response = redirect('/registr/')
    response.set_cookie('publicKey', PublicKeuSolana)
    return response
################


# страниса профиля игрока
@csrf_exempt
def profile_(request):
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(userv) == 0:
            return nereadres("registr")
    else:
        return nereadres("registr")
    user = userv[0]


    if request.method == 'POST':
        return profile_POST(request,user)
    elif request.method == 'GET':
        return profile_GET(request,user)
    else:
        printF("Eroor: registr_: request.method !=")
        return HttpResponse("Eroor")



def profile_GET(request,user):
    deita(user)

    NFT = NFTs.objects.filter(Pleir=user)
    NFTCOl = len(NFT)
    EnergiaMax = 0
    Energia = 0
    for i in NFT:
        EnergiaMax += i.EnergiaMax
        Energia += i.Energia

    return render(request, 'CryptoRunner/profil.html',
                  siteDeta(profile_neim, user, False,
                           {"tovar": NFT, "user": user,
                            "NFTCOl": NFTCOl, "EnergiaMax": EnergiaMax, "Energia": Energia,"zritel":False}))

def profile_POST(request,user):
    Jsons = json.loads(request.body.decode('utf-8'))

    y = Jsons["tip"]
    if y == "Nick":
        Date = Jsons["Date"]
        user.Nick = str(Date)
        user.save()
    else:
        return JsonResponse({"Eroor": True})
    return JsonResponse({"Eroor":False})



######################


# страниса профиля N игрока
def profileX_(request,profil):
    userv = Pleir.objects.filter(PublicKeuSolana=profil)
    if len(userv) == 0:
        userv = Pleir.objects.filter(pk=profil)
        if len(userv) == 0:
            return nereadres("Eroor404", "Eroor: profileX_: ползавател отсуттвует")
    user = userv[0]

    NFT = NFTs.objects.filter(Pleir=user)
    NFTCOl = len(NFT)
    EnergiaMax = 0
    Energia = 0
    for i in NFT:
        EnergiaMax += i.EnergiaMax
        Energia += i.Energia

    return render(request, 'CryptoRunner/profil.html',
                  siteDeta(profileX_neim, user, False, { "tovar": NFT,"user":user,
                    "NFTCOl":NFTCOl, "EnergiaMax": EnergiaMax, "Energia": Energia,"zritel":True}))

