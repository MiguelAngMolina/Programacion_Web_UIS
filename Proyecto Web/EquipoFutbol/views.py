#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

#importar modelo y formulario
from .models import EquipoFutbol
from .forms import EquipoFutbolForm
from .serializers import EquipoFutbolSerializer

#Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {}
    #respuesta
    return HttpResponse(template.render(context,request))

###### FRONT############################

def listarEquipoFutbol(request):
    Equipos = EquipoFutbol.objects.all()
    context = {'EquipoFutbol':Equipos}
    template = loader.get_template('EquipoFutbol/EquipoFutbol.html')
    return HttpResponse(template.render(context,request))

def EquipoFutbol_view(request, id):
    context = {}
    context['object'] = EquipoFutbol.objects.get(id = id)
    return render(request,'EquipoFutbol/EquipoFutbol_detalle.html',context)

def crear_EquipoFutbol(request):
    context = {}
    form = EquipoFutbolForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('EquipoFutbol')    
    context['form'] = form
    return render(request,'EquipoFutbol/crear_EquipoFutbol.html', context)


#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_EquipoFutbol(request,id):
    context = {}
    obj = get_object_or_404(EquipoFutbol, id = id)
    #formulario que contiene la instancia
    form = EquipoFutbolForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('EquipoFutbol')    
    context['form'] = form
    return render(request, "EquipoFutbol/actualizar_EquipoFutbol.html", context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(EquipoFutbol, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('EquipoFutbol')    
    return render(request, "EquipoFutbol/eliminar_EquipoFutbol.html", context)

##### API ########################




class EquipoListApiView(APIView):

    def get(self,request,*args, **kwargs):
        '''
        Lista todos las Equipos en base de datos
        '''
        Equipos = EquipoFutbol.objects.all()
        serializer = EquipoFutbolSerializer(Equipos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request, *args, **kwargs):
        '''
        Crea un equipo en base de datos
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'pais': request.data.get('pais'),
            'estadio': request.data.get('estadio'),
            'fechafundacion': request.data.get('fechafundacion'),
            'cantidadtitulos': request.data.get('cantidadtitulos'),
            'coloresequipacion': request.data.get('coloresequipacion'),
            'ciudad':request.data.get('ciudad')
            }

        serializer = EquipoFutbolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipoDetailApiView(APIView):

    def get_object(self,Equipo_id):
        '''
        Metodo de ayuda para retornar una Equipo con un id Dado
        '''
        try:
            return EquipoFutbol.objects.get(id=Equipo_id)
        except EquipoFutbol.DoesNotExist:
            return None
        
    def get(self,request,Equipo_id, *args, **kwargs):
        '''
        Permite obtener una equipo por ID
        '''
        Equipo_instance = self.get_object(Equipo_id)
        if not Equipo_instance:
            return Response(
                {"res":"El equipo con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        serializer = EquipoFutbolSerializer(Equipo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, Equipo_id, *args, **kwargs):
        '''
        Actualiza un equipo por su ID
        '''
        Equipo_instance = self.get_object(Equipo_id)
        if not Equipo_instance:
            return Response(
                {"res":"El Equipo con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'nombre': request.data.get('nombre'),
            'apellidos': request.data.get('apellido'),
            'idtipodocumento': request.data.get('idtipodocumento'),
            'documento': request.data.get('documento'),
            'lugarresidencia': request.data.get('lugarresidencia'),
            'fechanacimiento': request.data.get('fechanacimiento'),
            'email':request.data.get('email'),
            'telefono':request.data.get('telefono'),
            'usuario':request.data.get('usuario'),
            'password': request.data.get('password')
        }

        serializer = EquipoFutbolSerializer(instance = Equipo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,Equipo_id, *args, **kwargs):
        '''
        Elimina el equipo con el ID dado
        '''
        Equipo_instance = self.get_object(Equipo_id)
        if not Equipo_instance:
            return Response(
                {"res":"El equipo con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        Equipo_instance.delete()
        return Response(
            {"res":"Object Deleted"},
            status=status.HTTP_200_OK
        )