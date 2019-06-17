from django.db import models

class Persona(models.Model):
	Name = models.CharField(max_length=200)
	LastName = models.CharField(max_length=200)
	StartDate = models.DateTimeField('Starting date')
