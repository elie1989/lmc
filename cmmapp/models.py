from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Connexion(models.Model):
    Email= models.EmailField()
    Password= models.CharField(max_length=100)

class Sexe(models.Model):
    Sexe_patient = models.CharField(max_length=20)

class Groupesanguin(models.Model):
    Groupe_sanguin = models.CharField(max_length=150)

class EtatcivilPatient(models.Model):
    Etat_civil = models.CharField(max_length=80)

class EtatcivilAgent(models.Model):
    Etat_civil = models.CharField(max_length=80)

class Specialisation(models.Model):
    Specialisation = models.CharField(max_length=150)

class CategoriePatient(models.Model):
    Categorie_patient = models.CharField(max_length=150)

class CategorieAgent(models.Model):
    Categorie_agent = models.CharField(max_length=150)

class Localisation(models.Model):
    Commune = models.CharField(max_length=150)

class Patient(models.Model):
    Categorie_patient = models.ForeignKey(CategoriePatient,on_delete=models.CASCADE)
    Etat_civil = models.ForeignKey(EtatcivilPatient,on_delete=models.CASCADE)
    Commune = models.ForeignKey(Localisation,on_delete=models.CASCADE)
    Sexe = models.ForeignKey(Sexe,on_delete=models.CASCADE)
    Noms = models.CharField(max_length= 150)
    Profession = models.CharField(max_length=150)
    Date_naissance = models.DateField()
    Age = models.IntegerField()
    Adresse_physique = models.TextField()

class Agent(models.Model):
    Sexe = models.ForeignKey(Sexe,on_delete=models.CASCADE)
    specialisation = models.ForeignKey(Specialisation,on_delete=models.CASCADE)
    etatcivil = models.ForeignKey(EtatcivilAgent,on_delete=models.CASCADE)
    Categorie_Agent = models.ForeignKey(CategorieAgent,on_delete=models.CASCADE)
    Noms = models.CharField(max_length=150)
    Date_naissance = models.DateField()
    Age = models.IntegerField()
    

