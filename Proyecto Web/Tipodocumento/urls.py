from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('Tipodocumento/api/', views.TipoDocumentoListApiView.as_view()),
    path('Tipodocumento/api/<int:Tipodocumento_id>/', views.TipodocumentoDetailApiView.as_view()),
    path('Tipodocumento/', views.listarTipoDocumento, name='Tipodocumento'),
    path('Tipodocumento/new', views.crear_Tipodocumento, name='nuevo_Tipodocumento'),
    path('Tipodocumento/<id>/', views.Tipodocumento_view, name='Tipodocumento_view'),
    path('Tipodocumento/update/<id>/', views.update_Tipodocumento, name='Tipodocumento_actualizar'),
    path('Tipodocumento/delete/<id>/', views.delete_view, name='Tipodocumento_eliminar'),
]