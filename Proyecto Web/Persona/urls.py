from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('Persona/api/', views.PersonaListApiView.as_view()),
    path('Persona/api/<int:Persona_id>/', views.PersonaDetailApiView.as_view()),
    path('Persona/', views.listarPersona, name='Persona'),
    path('Persona/new', views.crear_Persona, name='nuevo_Persona'),
    path('Persona/<id>/', views.Persona_view, name='Persona_view'),
    path('Persona/update/<id>/', views.update_Persona, name='Persona_actualizar'),
    path('Persona/delete/<id>/', views.delete_view, name='Persona_eliminar'),
]