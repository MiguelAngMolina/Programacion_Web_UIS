from django.urls import path
from . import views

#definimos las rutas de la pagina de la app ciudad
urlpatterns = [
    #ruta, vista, nombre interno
    path('', views.index, name='index'),
    path('Ciudad/api/', views.CiudadListApiView.as_view()),
    path('Ciudad/api/<int:Ciudad_id>/', views.CiudadDetailApiView.as_view()),
    path('Ciudad/', views.listarCiudad, name='Ciudad'),
    path('Ciudad/new', views.crear_Ciudad, name='nuevo_Ciudad'),
    path('Ciudad/<id>/', views.Ciudad_view, name='Ciudad_view'),
    path('Ciudad/update/<id>/', views.update_Ciudad, name='Ciudad_actualizar'),
    path('Ciudad/delete/<id>/', views.delete_view, name='Ciudad_eliminar'),
]

