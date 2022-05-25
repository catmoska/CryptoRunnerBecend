from .logik import *
from datetime import datetime


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

        nft = NFTs.objects.filter(Pleir=userv)[int(data['NFTVID'])]

        userv.Money += float(data['Money'])
        userv.Distansion += float(data['Distansion'])
        userv.Record = float(data['Distansion'])
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

    A = None
    if hehNFT !=None:
        A = NoiskNft(nft, hehNFT)

    if A ==None:
        for i in nft:
            otvet += otvetPlus(i)
    else:
        i = nft[A]
        otvet += otvetPlus(i)
        for i in range(len(nft)):
            if A !=i:
                i = nft[i]
                otvet += otvetPlus(i)

    if userv.nonitka:
        userv.nonitka = False
        userv.save()
    return HttpResponse(otvet)

def otvetPlus(i):
    return str(i.Energia) + "&" + str(i.EnergiaMax) + "&" + str(i.Nick) + "&" + \
             str(0 if (i.Energia == i.EnergiaMax) else int(
                 (times - (datetime.now(timezone.utc) - i.DataVixada)).seconds / 60)) + "&" + \
             str(i.ClothesTip.pk) + "$"

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

