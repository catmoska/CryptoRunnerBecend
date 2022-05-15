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

    # def initi(self,PublicKeuSolana):
    #     self.DataRegistr = datetime.datetime.now()
    #     self.DataVixada = datetime.datetime.now()
    #     self.Energia = 20
    #     self.EnergiaMax = 20
    #     self.PublicKeuSolana = PublicKeuSolana
    #     # self.NFT = NFTs.objects.get(pk=1)
    #     # self.save()
    #     # return self.idHash


    # def __str__(self):
    #     return "Nick: "+self.Nick + \
    #            "n\ PublicKeuSolana: "+self.PublicKeuSolana+\
    #            "n\ Money: " + self.Money+\
    #            "n\ NFT N: " + len(self.NFT.objects.all())


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
    СlothesTip = models.ForeignKey("Сlothes",on_delete=models.CASCADE)
    # СlothesTipM = models.ForeignKey("Сlothes",on_delete=models.CASCADE)


    # def initi(self):
    #     self.Narameter ={}
    #     self.DataSozdania = datetime.datetime.now()
    #     self.DataVixada = datetime.datetime.now()
    #     self.Energia = 3
    #     self.EnergiaMax = 3
    #     self.idHash = sha256(self.pk.encode('utf-8')).hexdigest()
    #     self.save()



class Сlothes(models.Model):
    Photo = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True)



class MARKETPLACEmodel(models.Model):
    nft = models.ForeignKey("NFTs",on_delete=models.CASCADE)
    stoimost = models.FloatField(default=0.05)
    idHash = models.CharField(max_length=256)







# adminGj
# tyninsicGJstudiosC

