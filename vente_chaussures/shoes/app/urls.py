from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # payement urls

    path('liste-ventes/',views.getVentes),
    path('ajoute-vente/',views.createVentes),

]