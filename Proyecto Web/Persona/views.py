#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

#importar modelo y formulario
from .models import Persona
from .forms import PersonaForm
from .serializers import PersonaSerializer

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

#Vista para listar autores
def listarPersona(request):
    Personas = Persona.objects.all()
    context = {'Persona':Personas}
    template = loader.get_template('Persona/Persona.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un autor
def Persona_view(request, id):
    context = {}
    context['object'] = Persona.objects.get(id = id)
    return render(request,'Persona/Persona_detalle.html',context)

#vista para crear autores.
def crear_Persona(request):
    context = {}
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Persona')    
    context['form'] = form
    return render(request,'Persona/crear_Persona.html', context)


#vista para actualizar autores
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_Persona(request,id):
    context = {}
    obj = get_object_or_404(Persona, id = id)
    #formulario que contiene la instancia
    form = PersonaForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('Persona')    
    context['form'] = form
    return render(request, "Persona/actualizar_Persona.html", context)


#Vista para eliminar un autor
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Persona, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('Persona')    
    return render(request, "Persona/eliminar_Persona.html", context)

##### API ########################




class PersonaListApiView(APIView):

    def get(self,request,*args, **kwargs):
        '''
        Lista todos las Personas en base de datos
        '''
        Personas = Persona.objects.all()
        serializer = PersonaSerializer(Personas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request, *args, **kwargs):
        '''
        Crea una persona en base de datos
        '''
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

        serializer = PersonaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaDetailApiView(APIView):

    def get_object(self,Persona_id):
        '''
        Metodo de ayuda para retornar una persona con un id Dado
        '''
        try:
            return Persona.objects.get(id=Persona_id)
        except Persona.DoesNotExist:
            return None
        
    def get(self,request,Persona_id, *args, **kwargs):
        '''
        Permite obtener una persona por ID
        '''
        Persona_instance = self.get_object(Persona_id)
        if not Persona_instance:
            return Response(
                {"res":"La persona con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        serializer = PersonaSerializer(Persona_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, Persona_id, *args, **kwargs):
        '''
        Actualiza una persona por su ID
        '''
        Persona_instance = self.get_object(Persona_id)
        if not Persona_instance:
            return Response(
                {"res":"La persona con el id dado no existe"},
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

        serializer = PersonaSerializer(instance = Persona_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,Persona_id, *args, **kwargs):
        '''
        Elimina la persona con el ID dado
        '''
        Persona_instance = self.get_object(Persona_id)
        if not Persona_instance:
            return Response(
                {"res":"La persona con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        Persona_instance.delete()
        return Response(
            {"res":"Object Deleted"},
            status=status.HTTP_200_OK
        )