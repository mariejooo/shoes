from sqlite3 import PARSE_COLNAMES
from .models import Client , Chaussures , Vente
from rest_framework import serializers

class ClientSerialize(serializers.ModelSerializer):
    class Meta:
        model = Client

        fields = '__all__'

        id_client = serializers.CharField(required=True)
        nom = serializers.CharField(required=True)
        prenms = serializers.CharField(required=True)
        

class ChaussuresSerialize(serializers.ModelSerializer):

    class Meta:
        model = Chaussures

        fields =  '__all__'

    id_chaussures=  serializers.CharField(required=True)
    intitulé =  serializers.CharField(required=True)
    nbredispo =  serializers.CharField(required=True)
    prix_unitaire =  serializers.CharField(required=True)


class VenteSerialize(serializers.ModelSerializer):
    class Meta:
        model = Vente

        fields = '__all__'
    
    id_vente= serializers.CharField(required=True)
    id_client = serializers.CharField(required=True)
    quantiité = serializers.CharField(required=True)
    prix_unitaire = serializers.CharField(required=True)
