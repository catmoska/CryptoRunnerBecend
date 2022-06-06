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
        return render(request, 'CryptoRunner/registr.html', {'title': 'регистрасия'})
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
            DataRegistr=datetime_today(),
            DataVixada=datetime_today(),
            PublicKeuSolana=PublicKeuSolana,
            idHash=idHash, Energia=20, EnergiaMax=20, Money=moneu)
        y.save()
        
        # sozdaniaNft(y,1)

    response = redirect('/registr/')
    response.set_cookie('publicKey', PublicKeuSolana)
    return response
################


# страниса профиля игрока
def profile_(request):
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        printF(userv)
        if len(userv) == 0:
            return nereadres("registr")
    else:
        return nereadres("registr")
    user = userv[0]
    deita(user)

    NFT = NFTs.objects.filter(Pleir=user)
    NFTCOl = len(NFT)
    EnergiaMax =0
    Energia =0
    for i in NFT:
        EnergiaMax +=i.EnergiaMax
        Energia += i.Energia

    return render(request, 'CryptoRunner/profil.html',
                  {'title': 'profil', "tovar": NFT,"user":user,
                   "NFTCOl":NFTCOl,"EnergiaMax":EnergiaMax,"Energia":Energia})

# страниса профиля N игрока
def profileX_(request,profil):
    userv = Pleir.objects.filter(PublicKeuSolana=profil)
    if len(userv) == 0:
        return nereadres("Eroor404")
    user = userv[0]

    NFT = NFTs.objects.filter(Pleir = user)
    NFTCOl = len(NFT)

    return render(request, 'CryptoRunner/profil.html',
                  {'title': 'profil', "tovar": NFT,"user":user,"NFTCOl":NFTCOl})

