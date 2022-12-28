from django.shortcuts import render, redirect
from .models import  *
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def home(request):
    
    if request.method == "POST":
        data = (request.POST)
        asunto = "Consulta"
        de = data["email"]
        cuerpo = {
            "name": data["name"],
            "email": data["email"],
            "message": data["message"]
        }

        mensaje = "\n".join(cuerpo.values()) 

        try:
            send_mail(asunto,mensaje,de,["alejandro.enet1991@gmail.com"])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
            
            return render(request,"base/home.html",context)

        return redirect("home")
  
    
    return render(request,"base/home.html")

def projects_datascience(request):
    publication = Publication.objects.filter(type = "datascience")
    return render(request,"base/datascience_projects.html",{"publication":publication})

def projects_django(request):
    publication = Publication.objects.filter(type = "django")
    return render(request,"base/django_projects.html",{"publication":publication})

def cursos(request):
    return render(request,"base/cursos.html")