from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

def index(request):
	return HttpResponse("response working")

def edit(request):
	return render(request, 'namelist/main_page.html')

def details(request, Persona_id):
	personal = Persona.objects.all()
	return render(request, 'namelist/someone.html', {'personal':personal})

def sched_details(request, Persona_id):
	return	HttpResponse("you're lokking at %s's schedule", Persona_id)
# Create your views here.
