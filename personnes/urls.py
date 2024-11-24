from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_personne, name='create'),
    path('view/<int:id>/', views.view_personne, name='view'),
    path('about/', views.about, name='about'),
]


