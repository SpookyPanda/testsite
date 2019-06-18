from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('edit/', views.edit, name='edit'),
	path('<int:Persona_id>', views.details, name="details"),
	path('<int:Persona_id>/schedule', views.sched_details, name="sched_details"),
]