from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("response working")

def edit(request):
	return HttpResponse("Response still working")

# Create your views here.
