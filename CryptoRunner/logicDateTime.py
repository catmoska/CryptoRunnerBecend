from datetime import datetime,timezone,timedelta
from .models import *


times = timedelta(minutes=81)


def deita(user: Pleir):
    from datetime import datetime

    NFTSS = NFTs.objects.filter(Pleir=user)
    for nft in NFTSS:
        if nft.Energia != nft.EnergiaMax:
            timesVremina = datetime.now(timezone.utc) - nft.DataVixada
            nft.Energia += int(timesVremina / times)
            nft.DataVixada += int(timesVremina / times) * times
            if nft.Energia > nft.EnergiaMax:
                nft.Energia = nft.EnergiaMax
                nft.DataVixada = datetime.now(timezone.utc)
        else:
            nft.DataVixada = datetime.now(timezone.utc)
        nft.save()


def deitaNFT(nft: NFTs):
    from datetime import datetime

    if nft.Energia != nft.EnergiaMax:
        timesVremina = datetime.now(timezone.utc) - nft.DataVixada
        nft.Energia += int(timesVremina / times)
        nft.DataVixada += int(timesVremina / times) * times
        if nft.Energia > nft.EnergiaMax:
            nft.Energia = nft.EnergiaMax
            nft.DataVixada = datetime.now(timezone.utc)
    else:
        nft.DataVixada = datetime.now(timezone.utc)
    nft.save()
