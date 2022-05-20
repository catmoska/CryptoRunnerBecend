from django.db import models
from django.urls import reverse
import datetime
from hashlib import sha256



class Pleir(models.Model):
    # Nick = models.CharField(max_length=50,default="Pleir")
    idHash = models.CharField(max_length=256)
    PublicKeuSolana = models.CharField(max_length=50)
    Money = models.FloatField(default=0)
    Distansion = models.FloatField(default=0)
    Record = models.FloatField(default=0)
    DataRegistr = models.DateField()
    DataVixada = models.DateTimeField()
    # Energia = models.IntegerField()
    # EnergiaMax = models.IntegerField()
    isSiter = models.BooleanField(default=False)
    # plei = models.CharField(max_length=256,null=True)
    nonitka =models.BooleanField(default=True)

class NFTs(models.Model):
    Nick = models.CharField(max_length=20,default="defolt")
    # Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    idHash = models.CharField(max_length=256)
    Pleir = models.ForeignKey("Pleir",on_delete=models.CASCADE,null=True)
    # URLnft = models.CharField(max_length=20,default="")
    Energia = models.IntegerField()
    EnergiaMax = models.IntegerField()
    DataSozdania = models.DateField()
    DataVixada = models.DateTimeField()
    ClothesTip = models.ForeignKey("Сlothes",on_delete=models.CASCADE)
    # СlothesTipM = models.ForeignKey("Сlothes",on_delete=models.CASCADE)


class Сlothes(models.Model):
    Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)



class MARKETPLACEmodel(models.Model):
    nft = models.ForeignKey("NFTs",on_delete=models.CASCADE)
    stoimost = models.FloatField(default=0.05)







# adminGj
# tyninsicGJstudiosC

