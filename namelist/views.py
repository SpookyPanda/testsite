from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("response working")

# Create your views here.
