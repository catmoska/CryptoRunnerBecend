from logik import *

#################   разработка
@csrf_exempt
def sunduk_(request,N):
    registor= True
    if request.COOKIES:
        users = Pleir.objects.filter(PublicKeuSolana=request.COOKIES.get('publicKey'))
        if len(users) == 0:
            registor = False
    else:
        registor = False

    if registor:
        user =users[0]

    Box = Boks.objects.filter(pk=N)
    if len(Box) == 0:
        if request.method == 'POST':
            return JsonResponse({"Eroor": True})
        return nereadres("Eroor404")
    Box = Box[0]

    if request.method == 'GETPARAMS':
        return JsonResponse({"stoimost":Box.stoimost, "publickeusol":Glava})

    elif request.method == 'POST':
        if not registor:
            return JsonResponse({"Eroor":True})

        nft, idHash, cloat, tip = sozdaniaNftBox(user,Box)
        return JsonResponse({"urlStronisi":"nft/"+str(idHash),"urlImeig":cloat.Photo.url,"idHash":idHash,"Eroor":False})


    return render(request, 'CryptoRunner/sunduk.html',{'title':"sunduk",'N':N,"Bok":Box,"registor":registor})

#################

