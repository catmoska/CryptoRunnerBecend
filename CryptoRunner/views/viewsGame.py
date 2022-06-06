from .logik import *

################# работа с даними с unity
@csrf_exempt
def geimDETA_(request):
    # userv = Pleir.objects.filter(PublicKeuSolana="HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav")
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(userv) == 0:
            return HttpResponse("TestPleir")
    else:
        return HttpResponse("TestPleir")

    user = userv[0]

    # printF(request.method)
    if request.method == 'POSTBUI':
        return geimDETA_postBui(request,user)
    elif request.method == 'POST':
        return geimDETA_post(request,user)
    elif request.method == 'GET':
        return geimDETA_get(request,user)
    else:
        printF("Eroor: geimDETA_: request.method !=")
        return HttpResponse("Eroor")


def geimDETA_postBui(request,user):
    # data = json.loads(request.body.decode('utf-8'))
    if user.Money <= stoimostNftBoniCrint:
        return JsonResponse({"Eroor": True})

    user.Money -= stoimostNftBoniCrint
    user.save()

    Bok = Boks.objects.filter(pk=1)
    if len(Bok) == 0:
        printF("BokEroor")
        return JsonResponse({"Eroor": True})
    Bok = Bok[0]

    BokTip = [Bok.tip1, Bok.tip2, Bok.tip3, Bok.tip4]
    tip = resULTATBokTip(BokTip)
    nft,idHash,cloat = sozdaniaNft(user, tip)

    return JsonResponse(
        {"urlStronisi": "nft/" + str(idHash), "urlImeig": cloat.Photo.url, "idHash": idHash, "Eroor": False})


def geimDETA_post(request,user):
    data = convert(request.body.decode('utf-8'))
    if data['Nonztia'] == "1":
        nft = NFTs.objects.filter(Pleir=user)[int(data['NFTVID'])]
        nft.Energia += 1
        nft.DataVixada = datetime_now_F()
        user.Energia += 1
        nft.save()
        user.save()
        return HttpResponse("")

    nft = NFTs.objects.filter(Pleir=user)[int(data['NFTVID'])]

    user.Money += float(data['Money'])
    user.Distansion += float(data['Distansion'])
    user.Record = float(data['Distansion'])
    printF(nft.pk)
    if nft.Energia <= 0:
        printF("EroorNFTEnergia")
        return HttpResponse("EroorNFTEnergia")
    if nft.Energia == nft.EnergiaMax:
        nft.DataVixada = datetime_now_F()
    nft.Energia -= 1
    user.save()
    nft.save()
    deita(user)
    t = HttpResponse("")
    t.set_cookie('NFThistori', nft.idHash)
    return t


def geimDETA_get(request,user):
    hehNFT = request.COOKIES.get('NFThistori')
    deita(user)
    nft = NFTs.objects.filter(Pleir=user)
    if len(nft) == 0:
        return HttpResponse("EroorNFT")

    otvet = str(user.Money) + "&" + str(user.Record) + \
            "&" + str(user.nonitka) + "&" + str(stoimostNftBoniCrint) + "$"

    A = None
    if hehNFT != None:
        A = NoiskNft(nft, hehNFT)

    if A == None:
        for i in nft:
            otvet += geimDETA_otvetPlus(i)
    else:
        i = nft[A]
        if i.Energia == 0:
            for i in nft:
                otvet += geimDETA_otvetPlus(i)
        else:
            otvet += geimDETA_otvetPlus(i)
            for i in range(len(nft)):
                if A != i:
                    i = nft[i]
                    otvet += geimDETA_otvetPlus(i)

    if user.nonitka:
        user.nonitka = False
        user.save()
    return HttpResponse(otvet)


def geimDETA_otvetPlus(i):
    return str(i.Energia) + "&" + str(i.EnergiaMax) + "&" + "Runner: #"+str(i.pk) + "&" + \
             str(0 if (i.Energia == i.EnergiaMax) else int(
            (times - (datetime_now_F() - i.DataVixada)).seconds / 60)) + "&" + \
             str(i.ClothesTip.pk) + "$"

###############################
''''''


# страниса игри
def geim_(request):
    if request.COOKIES:
        if request.COOKIES.get('publicKey') == None:
            return nereadres("registr")
        user = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(user) == 0:
            return nereadres("registr")
        else:
            nft = NFTs.objects.filter(Pleir=user[0])
            if len(nft) == 0:
                return nereadres("MARKETPLACE")
    else:
        return nereadres("registr")

    resultat = render(request, 'CryptoRunner/geim.html', {'title': 'geim'})
    return resultat

