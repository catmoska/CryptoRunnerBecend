from .logik import *



############# техническая страниса по виставке NFT
def nftVistavka_(request):
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
        return nftVistavka_POST(request)
    elif request.method == 'GET':
        return render(request, 'CryptoRunner/nftVistavka.html', {"form":NewForms()})
    else:
        printF("Eroor: nftCilka_: request.method !=")
        return HttpResponse("Eroor")

def nftVistavka_POST(request):
    form = NewForms(request.POST)
    pleir = Pleir.objects.filter(PublicKeuSolana="AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw")
    if len(pleir) == 0:
        y = Pleir(
            DataRegistr=datetime_today(),
            DataVixada=datetime_today(),
            PublicKeuSolana="AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw",
            idHash="", Energia=0, EnergiaMax=0, Money=0)
        y.save()
        pleir = [y]
    pleir = pleir[0]

    if form.is_valid():
        colisestvo = form.cleaned_data["colisestvo"]
        stoimostStart = form.cleaned_data["stoimostStart"]
        Neriod = form.cleaned_data["Neriod"]
        Tip = int(form.cleaned_data["Tip"]) - 1

        for i in range(colisestvo):
            nft =sozdaniaNft(pleir, Tip)
            R = MARKETPLACEmodel(nft=nft, stoimost=round((stoimostStart + Neriod * i), 5))
            R.save()
    return nereadres("MARKETPLACE")

###########


def referalni_(request, referalni):
    response = redirect('/')
    response.set_cookie('referalnaiSika', referalni)
    return response
