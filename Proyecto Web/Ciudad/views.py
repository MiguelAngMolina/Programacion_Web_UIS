#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

#Modelos
from .models import Ciudad
from .forms import CiudadForm
from .serializers import CiudadSerializer

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

def listarCiudad(request):
    Ciudades = Ciudad.objects.all()
    context = {'Ciudad':Ciudades}
    template = loader.get_template('Ciudad/Ciudad.html')
    return HttpResponse(template.render(context,request))

def Ciudad_view(request, id):
    context = {}
    context['object'] = Ciudad.objects.get(id = id)
    return render(request,'Ciudad/Ciudad_detalle.html',context)

#vista para crear tipo documentos.
def crear_Ciudad(request):
    context = {}
    form = CiudadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Ciudad')    
    context['form'] = form
    return render(request,'Ciudad/crear_Ciudad.html', context)


#vista para actualizar tipo documentos
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_Ciudad(request,id):
    context = {}
    obj = get_object_or_404(Ciudad, id = id)
    #formulario que contiene la instancia
    form = CiudadForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('Ciudad')    
    context['form'] = form
    return render(request, "Ciudad/actualizar_Ciudad.html", context)


#Vista para eliminar una ciudad
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Ciudad, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('Ciudad')    
    return render(request, "Ciudad/eliminar_Ciudad.html", context)



class CiudadListApiView(APIView):

    def get(self,request,*args, **kwargs):
        '''
        Lista todos los libros en base de datos
        '''
        Ciudades = Ciudad.objects.all()
        serializer = CiudadSerializer(Ciudades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request, *args, **kwargs):
        '''
        Crea un libro en base de datos
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion')
        }

        serializer = CiudadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CiudadDetailApiView(APIView):

    def get_object(self,Ciudad_id):
        '''
        Metodo de ayuda para retornar un libro con un id Dado
        '''
        try:
            return Ciudad.objects.get(id=Ciudad_id)
        except Ciudad.DoesNotExist:
            return None
        
    def get(self,request,Ciudad_id, *args, **kwargs):
        '''
        Permite obtener un libro por ID
        '''
        Ciudad_instance = self.get_object(Ciudad_id)
        if not Ciudad_instance:
            return Response(
                {"res":"El libro con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        serializer = CiudadSerializer(Ciudad_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,Ciudad_id, *args, **kwargs):
        '''
        Actualiza un libro por su ID
        '''
        Ciudad_instance = self.get_object(Ciudad_id)
        if not Ciudad_instance:
            return Response(
                {"res":"La ciudad con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion')
        }

        serializer = CiudadSerializer(instance = Ciudad_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,Ciudad_id, *args, **kwargs):
        '''
        Elimina el libro con el ID dado
        '''
        Ciudad_instance = self.get_object(Ciudad_id)
        if not Ciudad_instance:
            return Response(
                {"res":"La ciudad con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        Ciudad_instance.delete()
        return Response(
            {"res":"Object Deleted"},
            status=status.HTTP_200_OK
        )
