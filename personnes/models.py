from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    ecole = models.CharField(max_length=100)
    experience = models.TextField()
    contact = models.TextField()
    diplome = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    date_naissance = models.DateField()
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    #date_creation = models.DateTimeField(auto_now_add=True)   Date de création
    #date_modification = models.DateTimeField(auto_now=True)   Date de dernière modification

    def __str__(self):
        return f"{self.nom} {self.prenom}"
