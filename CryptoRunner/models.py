from django.db import models
from django.urls import reverse
import datetime
from hashlib import sha256



class Pleir(models.Model):
    Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    Nick = models.CharField(max_length=50,default="Pleir")
    idHash = models.CharField(max_length=256)
    PublicKeuSolana = models.CharField(max_length=50)
    Money = models.FloatField(default=0)
    Distansion = models.FloatField(default=0)
    Record = models.FloatField(default=0)
    DataRegistr = models.DateField()
    DataVixada = models.DateTimeField()
    # Energia = models.IntegerField()
    # EnergiaMax = models.IntegerField()
    # isSiter = models.BooleanField(default=False)
    nonitka = models.BooleanField(default=True)


class NFTs(models.Model):
    Nick = models.CharField(max_length=20,default="defolt")
    idHash = models.CharField(max_length=256)
    Pleir = models.ForeignKey("Pleir",on_delete=models.CASCADE,null=True)
    Energia = models.IntegerField()
    EnergiaMax = models.IntegerField()
    DataSozdania = models.DateField()
    DataVixada = models.DateTimeField()
    ClothesTip = models.ForeignKey("Сlothes",on_delete=models.CASCADE)
    Tip = models.IntegerField(default=1)
    Ymnozitel = models.FloatField(default=1)
    geim = models.IntegerField(default=0)


class Сlothes(models.Model):
    Photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    PhotoNFT = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)


class MARKETPLACEmodel(models.Model):
    nft = models.ForeignKey("NFTs",on_delete=models.CASCADE)
    stoimost = models.FloatField(default=0.05)


class Boks(models.Model):
    Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    nik = models.CharField(max_length=256,default="Defolt")
    stoimost = models.FloatField(default=0.05)
    tip1 =models.FloatField(default=25)
    tip2 = models.FloatField(default=25)
    tip3 = models.FloatField(default=25)
    tip4 = models.FloatField(default=25)
    geim = models.IntegerField(default=0)
    otkritas = models.BooleanField(default=True)



"""
подготовка бази даних 
1 создания бд
    python manage.py makemigrations CryptoRunner
    python manage.py migrate
2 создания админки
    python manage.py createsuperuser
3 создания NFT
    нузна создать хоть одно nft
4 создания Box
    нузна создать одно Box (другий бокси не как не роботают)
всо
"""

# python manage.py collectstatic
# adminGj
# tyninsicGJstudiosC
