from .logik import *
from datetime import datetime ,timezone


@csrf_exempt
def geimDETA(request):
    hehNFT = None
    # userv = Pleir.objects.filter(PublicKeuSolana="HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav")
    if request.COOKIES:
        userv = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(userv) == 0:
            return HttpResponse("TestPleir")
        hehNFT = request.COOKIES.get('NFThistori')
    else:
        return HttpResponse("TestPleir")
    userv = userv[0]

    # print(request.method)
    if request.method == 'POSTBUI':
        data = json.loads(request.body.decode('utf-8'))
        # print(userv.Money)
        if userv.Money <=stoimostNftBoniCrint:
            return JsonResponse({"Eroor":True})

        userv.Money -= stoimostNftBoniCrint
        userv.save()

        Bok = Boks.objects.filter(pk=1)
        # print(len(Bok))
        if len(Bok) == 0:
            return JsonResponse({"Eroor":True})
        Bok = Bok[0]

        kolisestvo =len(NFTs.objects.all())
        kolisestvoCloat = len(Сlothes.objects.all())
        cloat = Сlothes.objects.all()[random.randint(0, kolisestvoCloat - 1)]
        BokTip = [Bok.tip1,Bok.tip2,Bok.tip3,Bok.tip4]
        res = resULTATBokTip(BokTip)
        hes = (str(datetime.now(timezone.utc)) + str(random.randint(-100, 100))) * random.randint(1, 3)
        idHash = sha224(hes.encode('utf-8')).hexdigest()
        nft = NFTs(
            Nick="Bonny NFT#" + str(kolisestvo+1),
            Energia=EnergiaSpisok[res], EnergiaMax=EnergiaSpisok[res],
            idHash=idHash, DataSozdania=datetime.now(timezone.utc),
            DataVixada=datetime.now(timezone.utc),
            Pleir=userv, ClothesTip=cloat, Ymnozitel=Ymnozitel[res])
        nft.save()
        # print(userv.Money)
        # print("dasdasd")
        return JsonResponse({"urlStronisi":"nft/"+str(idHash),"urlImeig":cloat.Photo.url,"idHash":idHash,"Eroor":False})

    if request.method == 'POST':
        data = convert(request.body.decode('utf-8'))
        if data['Nonztia'] == "1":
            nft = NFTs.objects.filter(Pleir=userv)[int(data['NFTVID'])]
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
        print(nft.pk)
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

    otvet = str(userv.Money) + "&" + str(userv.Record) + "&" + str(userv.nonitka) + "&"+ str(stoimostNftBoniCrint)+ "$"
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
    return str(i.Energia) + "&" + str(i.EnergiaMax) + "&" + "Runner: #"+str(i.pk) + "&" + \
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
            if len(nft) == 0:
                return nereadres("MARKETPLACE")
    else:
        return nereadres("registr")

    resultat = render(request, 'CryptoRunner/geim.html', {'title': 'geim'})
    # resultat.get_session_cookie_age("ddd","")
    return resultat

