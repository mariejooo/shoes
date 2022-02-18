from django.db import models


# Create your models here.
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    class Meta:
        db_table = 'client'


class Vente(models.Model):
    id_vente= models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client,db_column="idClient",related_name='idClient')
    id_chaussures= models.ForeignKey(Chaussures,db_column="idChaussures",related_name='idChaussures')
    quantiité = models.IntegerField()
    class Meta:
        db_table = 'vente'

class Chaussures(models.Model):
    id_chaussures= models.AutoField(primary_key=True)
    intitulé = models.CharField(max_length=255)
    nbredispo = models.CharField(max_length=255)
    prix_unitaire = models.IntegerField(max_length=255)
    class Meta:
        db_table = 'chaussures'
