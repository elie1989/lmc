from django.shortcuts import render

# Create your views here.

# Connexion cmm

def connexion(request):
    return render (request, "connexion.html")

# Vues patients

def ajoutpatient(request):
    return render (request,"ajoutpatient.html")

def listepatient(request):
    return render (request,"listepatient.html")

def suppressionpatient(request):
    return render (request,"")

# Vues agents

def ajoutagent(request):
    return render (request, "ajoutagent.html")

def listeagent(request):
    return render (request,"listeagentt.html")

def suppressionpatient(request):
    return render (request,"")






