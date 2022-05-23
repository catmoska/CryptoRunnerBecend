from .logik import *


@csrf_exempt
def MARKETPLACE(request):
    MARKETPLACE = MARKETPLACEmodel.objects.all()
    return render(request, 'CryptoRunner/MARKETPLACE.html',
                  {'title': 'MARKETPLACE', "tovar": MARKETPLACE,"stronisa":True})


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
        return nftCilkaPOST(data,nft,users[0])

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
     "pleir": pleir, "stoimost": stoimost,"registor":registor,"stronisa":True})

    response.set_cookie('NFThistori', nftHeh)

    return response


