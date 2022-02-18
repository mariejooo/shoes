from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client , Chaussures , Vente
from .serializers import ClientSerialize , ChaussuresSerialize , VenteSerialize
from rest_framework.decorators import   api_view , renderer_classes
import json
import os 

# Create your views here.
