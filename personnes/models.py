from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    ecole = models.CharField(max_length=200)
    experience = models.TextField()
    contact = models.CharField(max_length=15)
    diplome = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    date_naissance = models.DateField()
    genre = models.CharField(max_length=10, choices=[('Homme', 'Homme'), ('Femme', 'Femme')])

    def __str__(self):
        return f"{self.nom} {self.prenom}"
