from .logik import *
from .viewsStronisi import Eroor404
from datetime import datetime, timezone

EnergiaSpisok =[3,5,7,9]
Ymnozitel = [1, 1.5, 2, 3]


# @cache_page(60 * 60)
def pageNotFound(request, exception):
    return HttpResponseNotFound(Eroor404(request))


def nftVistavka(request):
    ppublic = ["HmTk4zFbTgnwApgmnBiCtfMaBfwdwuh3h2CjNaLvpHav",
               "871FK4JkgGDsQB7nDwgcTPJ8KR1ErE9nHd6L8cXQFopY",
               "AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw"]
    if request.COOKIES:
        users = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(users) == 0:
            return nereadres("registr")
        y =False
        for i in ppublic:
            if request.COOKIES.get('publicKey') == i:
                y = True
                pass
        if not y:
            return nereadres("main")
    else:
        return nereadres("main")

    if request.method == 'POST':
        form = NewForms(request.POST)
        pleir = Pleir.objects.filter(PublicKeuSolana="AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw")
        if len(pleir)==0:
            y = Pleir(
                DataRegistr=datetime.today(),
                DataVixada=datetime.today(),
                PublicKeuSolana="AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw",
                idHash="", Energia=0, EnergiaMax=0, Money=0)
            y.save()
            pleir = [y]
        pleir=pleir[0]

        if form.is_valid():
            colisestvo = form.cleaned_data["colisestvo"]
            stoimostStart = form.cleaned_data["stoimostStart"]
            Neriod = form.cleaned_data["Neriod"]
            # startSislo = form.cleaned_data["startSislo"]
            Tip = int(form.cleaned_data["Tip"])-1

            for i in range(colisestvo):
                kolisestvoCloat = len(Сlothes.objects.all())
                if kolisestvoCloat>1:
                    cloat = Сlothes.objects.all()[random.randint(0,kolisestvoCloat-1)]
                else:
                    cloat = Сlothes.objects.all()[0]
                hes = (str(datetime.now(timezone.utc))+str(random.randint(-100, 100)))*random.randint(1, 3)
                idHash = sha224(hes.encode('utf-8')).hexdigest()
                Energia = EnergiaSpisok[Tip]
                kolisestvo = len(NFTs.objects.all())
                nft = NFTs(
                    Nick="Bonny NFT#" + str(kolisestvo+1),
                    Energia=Energia, EnergiaMax=Energia,
                    idHash=idHash, DataSozdania=datetime.now(timezone.utc),
                    DataVixada=datetime.now(timezone.utc),
                    Pleir=pleir,ClothesTip=cloat,Ymnozitel=Ymnozitel[Tip])
                nft.save()
                R = MARKETPLACEmodel(nft=nft, stoimost=round((stoimostStart+Neriod*i),5))
                R.save()
        return nereadres("MARKETPLACE")
    elif request.method == 'GET':
        form = NewForms()
        return render(request, 'CryptoRunner/nftVistavka.html', {"form":form})
    return HttpResponse("Eroor")


def referalni(request, referalni):
    response = redirect('/')
    response.set_cookie('referalnaiSika', referalni)
    return response
