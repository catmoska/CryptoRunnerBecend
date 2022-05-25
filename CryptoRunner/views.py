from .viewsGame import *
from .viewsProfil import *
from .viewsTexnisesci import *
from .viewsStronisi import *
from .viewsMarketplace import *
from .logik import *

EnergiaSpisok =[3,5,7,9]
Ymnozitel = [1, 1.5, 2, 3]
Glava = "AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw"

@csrf_exempt
def sunduk(request,N):
    registor= True
    if request.COOKIES:
        users = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(users) == 0:
            registor = False
    else:
        registor = False
    if registor:
        user =users[0]

    Bok = Boks.objects.filter(pk=N)
    if len(Bok) == 0:
        return nereadres("Eroor404")
    Bok = Bok[0]

    if request.method == 'GETPARAMS':
        Bok = Boks.objects.get(pk=N)
        return JsonResponse({"stoimost":Bok.stoimost,"publickeusol":Glava})


    if request.method == 'POST':
        if not registor:
            return JsonResponse({"Eroor":True})

        kolisestvo =len(NFTs.objects.all())
        kolisestvoCloat = len(Сlothes.objects.all())
        cloat = Сlothes.objects.all()[random.randint(0, kolisestvoCloat - 1)]
        BokTip = [Bok.tip1,Bok.tip2,Bok.tip3,Bok.tip4]
        res = resULTATBokTip(BokTip)
        from datetime import datetime
        cloat = Сlothes.objects.all()[random.randint(0, 1)]
        hes = (str(datetime.now(timezone.utc)) + str(random.randint(-100, 100))) * random.randint(1, 3)
        idHash = sha224(hes.encode('utf-8')).hexdigest()
        nft = NFTs(
            Nick="Bonny NFT#" + str(kolisestvo+1),
            Energia=EnergiaSpisok[res], EnergiaMax=EnergiaSpisok[res],
            idHash=idHash, DataSozdania=datetime.now(timezone.utc),
            DataVixada=datetime.now(timezone.utc),
            Pleir=user, ClothesTip=cloat, Ymnozitel=Ymnozitel[res])
        nft.save()
        return JsonResponse({"urlStronisi":"nft/"+str(idHash),"urlImeig":cloat.Photo.url,"idHash":idHash,"Eroor":True})


    return render(request, 'CryptoRunner/sunduk.html',{'title':"",'N':N,"Bok":Bok,"registor":registor})


def resULTATBokTip(BokTip):
    resO = -1
    while True:
        random100 = random.randint(1, 99)
        res = 0
        q = 0
        for i in BokTip:
            if random100 > res:
                res += i
                q += 1
            elif random100 < res:
                resO = q

            if resO != -1:
                break
        if resO != -1:
            break
    return resO