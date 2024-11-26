from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse = models.TextField()
    ecole = models.CharField(max_length=100)
    experience = models.TextField()
    contact = models.CharField(max_length=20)
    diplome = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    date_naissance = models.DateField()
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])

    def __str__(self):
        return f"{self.nom} {self.prenom}"
