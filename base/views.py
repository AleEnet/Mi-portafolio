from django.shortcuts import render, redirect
from .models import  *
from .forms import ContactForm, UserRegisterForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

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



def register_user(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'base/register_user.html', context)