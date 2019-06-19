from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("response working")

def edit(request):
	return render(request, 'namelist/main_page.html')

def details(request, Persona_id):
	return HttpResponse("You're looking at %s", Persona_id)

def sched_details(request, Persona_id):
	return	HttpResponse("you're lokking at %s's schedule", Persona_id)
# Create your views here.
