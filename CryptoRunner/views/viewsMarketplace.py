from .logik import *

# страниса маркет плеиса (г - логика)
@csrf_exempt
def MARKETPLACE_(request):
    MARKETPLACE = MARKETPLACEmodel.objects.all()
    return render(request, 'CryptoRunner/MARKETPLACE.html',
                           {'title': MARKETPLACE_neim, "tovar": MARKETPLACE,"stronisa":True})



########### страниса NFT
@csrf_exempt
def nftCilka_(request, nftHeh):
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

    if request.method == 'GETPARAMS':
        return nftCilka_GETPARAMS(nft)
    elif request.method == 'POST':
        return nftCilka_POST(request,registor,nft,users)
    elif request.method == 'GET':
        return nftCilka_GET(request,registor,nft,users,nftHeh)
    else:
        printF("Eroor: nftCilka_: request.method !=")
        return HttpResponse("Eroor")


def nftCilka_GETPARAMS(nft):
    MARKETPLACE = MARKETPLACEmodel.objects.filter(nft=nft)
    if len(MARKETPLACE) == 0:
        return HttpResponse("ErorEczemplar")
    MARKETPLACE = MARKETPLACE[0]

    return JsonResponse(
        {"stoimost": MARKETPLACE.stoimost,
         "publickeusol": MARKETPLACE.nft.Pleir.PublicKeuSolana})


def nftCilka_POST(request,registor,nft,user):
    user = user[0]
    if not registor:
        return JsonResponse({"Eroor": True})
    data = json.loads(request.body.decode('utf-8'))

    printF(data["onerasia"])
    if data["onerasia"] == "bui":
        #######################################
        # printF(data)
        # nroverka(data["signatura"])
        # printF("das")
        #######################################
        nft.Pleir = user
        nft.save()
        marc = MARKETPLACEmodel.objects.filter(nft=nft)
        marc.delete()
    elif data["onerasia"] == "sell":
        marc = MARKETPLACEmodel.objects.filter(nft=nft)
        if len(marc) == 0:
            R = MARKETPLACEmodel(nft=nft, stoimost=round(float(data["prise"]), 5))
            R.save()
    elif data["onerasia"] == "take off":
        marc = MARKETPLACEmodel.objects.filter(nft=nft)
        marc.delete()
    return HttpResponse("")
    return nftCilkaPOST(data, nft, users[0])


def nftCilka_GET(request,registor,nft,users,nftHeh):
    deitaNFT(nft)
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
                      siteDeta('nft', users[0], True, {"NFT": nft, "market": marxet,
                       "pleir": pleir, "stoimost": stoimost, "registor": registor}))
    response.set_cookie('NFThistori', nftHeh)
    return response

##########################

