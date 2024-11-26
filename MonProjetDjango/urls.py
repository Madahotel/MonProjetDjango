"""
URL configuration for MonProjetDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personnes.urls')),
]


from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    personnes = Personne.objects.all()
    return render(request, 'personnes/home.html', {'personnes': personnes})

def create_personne(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        adresse = request.POST['adresse']
        ecole = request.POST['ecole']
        experience = request.POST['experience']
        contact = request.POST['contact']
        diplome = request.POST['diplome']
        language = request.POST['language']
        date_naissance = request.POST['date_naissance']
        genre = request.POST['genre']

        Personne.objects.create(
            nom=nom, prenom=prenom, adresse=adresse, ecole=ecole, experience=experience,
            contact=contact, diplome=diplome, language=language,
            date_naissance=date_naissance, genre=genre
        )
        return redirect('home')
    return render(request, 'personnes/create.html')

def view_personne(request, id):
    personne = get_object_or_404(Personne, id=id)
    return render(request, 'personnes/view.html', {'personne': personne})

def about(request):
    return render(request, 'personnes/about.html')
