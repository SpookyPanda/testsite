from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("response working")

def edit(request):
	return HttpResponse("Response still working")

def details(request, Persona_id):
	return HttpResponse("You're looking at %s", Persona_id)
	#comment

def sched_details(request, Persona_id):
	return	HttpResponse("you're lokking at %s's schedule", Persona_id)
# Create your views here.
