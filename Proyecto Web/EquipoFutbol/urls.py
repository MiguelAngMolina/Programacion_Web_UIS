from django.urls import path
from . import views

#definimos las rutas de la pagina de la app ciudad
urlpatterns = [
    #ruta, vista, nombre interno
    path('', views.index, name='index'),
    path('EquipoFutbol/api/', views.EquipoListApiView.as_view()),
    path('EquipoFutbol/api/<intEquipoFutbol_id>/', views.EquipoDetailApiView.as_view()),
    path('EquipoFutbol/', views.listarEquipoFutbol, name='EquipoFutbol'),
    path('EquipoFutbol/new', views.crear_EquipoFutbol, name='nuevo_EquipoFutbol'),
    path('EquipoFutbol/<id>/', views.EquipoFutbol_view, name='EquipoFutbol_view'),
    path('EquipoFutbol/update/<id>/', views.update_EquipoFutbol, name='EquipoFutbol_actualizar'),
    path('EquipoFutbol/delete/<id>/', views.delete_view, name='EquipoFutbol_eliminar')
]

