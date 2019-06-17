from django.db import models

class Question(models.Model):
	qnombre = models.CharField(max_length=100)
	qapellido = models.CharField(max_length=100)

class Answer(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)

# Create your models here.
