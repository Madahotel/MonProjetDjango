from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajouter/', views.ajouter_personne, name='ajouter_personne'),
    path('voir/', views.liste_personnes, name='liste_personnes'),
    path('profil/<int:id>/', views.profil_personne, name='profil_personne'),
    path('about/', views.about, name='about'), 
]
