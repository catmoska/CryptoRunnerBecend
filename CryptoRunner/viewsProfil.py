from .logik import *


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

        from datetime import datetime
        if len(snis) != 0:
            y = snis[0]
            y.DataVixada = datetime.now(timezone.utc)
            y.save()
        else:
            moneu =0
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


def profile(request):
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(userv) == 0:
            return nereadres("registr")
    else:
        return nereadres("registr")
    user = userv[0]
    deita(user)

    NFT = NFTs.objects.filter(Pleir = user)
    NFTCOl = len(NFT)

    return render(request, 'CryptoRunner/profil.html',
                  {'title': 'profil', "tovar": NFT,"user":user,"NFTCOl":NFTCOl})


def profileZ(request,profil):
    userv = Pleir.objects.filter(PublicKeuSolana=profil)
    if len(userv) == 0:
        return nereadres("Eroor404")
    user = userv[0]

    NFT = NFTs.objects.filter(Pleir = user)
    NFTCOl = len(NFT)

    return render(request, 'CryptoRunner/profil.html',
                  {'title': 'profil', "tovar": NFT,"user":user,"NFTCOl":NFTCOl})

