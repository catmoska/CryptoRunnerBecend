from django.db import models
from django.urls import reverse
import datetime
from hashlib import sha256



class Pleir(models.Model):
    # Nick = models.CharField(max_length=50,default="Pleir")
    idHash = models.CharField(max_length=256)
    PublicKeuSolana = models.CharField(max_length=50)
    # Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True, blank=True)
    Money = models.FloatField(default=0)
    Distansion = models.FloatField(default=0)
    Record = models.FloatField(default=0)
    DataRegistr = models.DateField()
    DataVixada = models.DateTimeField()
    Energia = models.IntegerField()
    EnergiaMax = models.IntegerField()
    isSiter = models.BooleanField(default=False)
    # plei = models.CharField(max_length=256,null=True)
    nonitka =models.BooleanField(default=True)

    def initi(self,PublicKeuSolana):
        self.DataRegistr = datetime.datetime.now()
        self.DataVixada = datetime.datetime.now()
        self.Energia = 20
        self.EnergiaMax = 20
        self.PublicKeuSolana = PublicKeuSolana
        # self.NFT = NFTs.objects.get(pk=1)
        # self.save()
        # return self.idHash


    def __str__(self):
        return "Nick: "+self.Nick + \
               "n\ PublicKeuSolana: "+self.PublicKeuSolana+\
               "n\ Money: " + self.Money+\
               "n\ NFT N: " + len(self.NFT.objects.all())


class NFTs(models.Model):
    Nick = models.CharField(max_length=20,default="defolt")
    # Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    idHash = models.CharField(max_length=256)
    idHashPleir = models.CharField(max_length=256)
    URLnft = models.CharField(max_length=20,default="")
    Obrabotka = models.BooleanField(default=False)
    Energia = models.IntegerField()
    EnergiaMax = models.IntegerField()
    DataSozdania = models.DateField()
    DataVixada = models.DateTimeField()
    # Narameter = models.JSONField()

    skin = models.IntegerField()
    suit = models.IntegerField()
    trousers = models.IntegerField()
    cap = models.IntegerField()
    gloves = models.IntegerField()

    def initi(self):
        self.Narameter ={}
        self.DataSozdania = datetime.datetime.now()
        self.DataVixada = datetime.datetime.now()
        self.Energia = 3
        self.EnergiaMax = 3
        self.idHash = sha256(self.pk.encode('utf-8')).hexdigest()
        self.save()

    # def __str__(self):
    #     return "Nick: " + self.Nick + \
    #            "n\ idHash: " + self.idHash + \
    #            "n\ Obrabotka: " + self.Obrabotka + \
    #            "n\ Narameter: " + self.Narameter




class Сlothes(models.Model):
    Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
    Narameter = models.JSONField()
    classСlothes = models.IntegerField()



# class MARKETPLACEmodel(models.Model):
#     Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)
#     nft = models.ForeignKey("NFTs")


