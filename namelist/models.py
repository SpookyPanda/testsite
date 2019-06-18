from django.db import models

class Persona(models.Model):
	Name = models.CharField(max_length=200)
	LastName = models.CharField(max_length=200)
	StartDate = models.DateTimeField('Starting date')


	def __str__(self):
		return self.Name

class Schedule(Persona):
	CheckIn = models.DateTimeField('Check in')
	CheckOut = models.DateTimeField('Check out')
