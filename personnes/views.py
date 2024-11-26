from django.shortcuts import render, get_object_or_404, redirect
from .models import Personne

def index(request):
    return render(request, 'personnes/index.html')

def ajouter_personne(request):
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
            contact=contact, diplome=diplome, language=language, date_naissance=date_naissance, genre=genre
        )
        return redirect('liste_personnes')
    return render(request, 'personnes/ajouter.html')

def liste_personnes(request):
    personnes = Personne.objects.all()
    return render(request, 'personnes/liste.html', {'personnes': personnes})

def profil_personne(request, id):
    personne = get_object_or_404(Personne, id=id)
    return render(request, 'personnes/profil.html', {'personne': personne})

def about(request):
    return render(request, 'personnes/about.html')
