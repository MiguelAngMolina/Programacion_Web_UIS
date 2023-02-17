#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

#Imports modelo y formulario
from .models import Tipodocumento
from .forms import TipodocumentoForm
from .serializers import TipoDocumentoSerializer

#Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def index(request):
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {}
    #respuesta
    return HttpResponse(template.render(context,request))

def listarTipoDocumento(request):
    tipoDocumentos = Tipodocumento.objects.all()
    context = {'Tipodocumento':tipoDocumentos}
    template = loader.get_template('Tipodocumento/Tipodocumento.html')
    return HttpResponse(template.render(context,request))

def Tipodocumento_view(request, id):
    context = {}
    context['object'] = Tipodocumento.objects.get(id = id)
    return render(request,'Tipodocumento/Tipodocumento_detalle.html',context)

#vista para crear tipo documentos.
def crear_Tipodocumento(request):
    context = {}
    form = TipodocumentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Tipodocumento')    
    context['form'] = form
    return render(request,'Tipodocumento/crear_Tipodocumento.html', context)


#vista para actualizar tipo documentos
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_Tipodocumento(request,id):
    context = {}
    obj = get_object_or_404(Tipodocumento, id = id)
    #formulario que contiene la instancia
    form = TipodocumentoForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('Tipodocumento')    
    context['form'] = form
    return render(request, "Tipodocumento/actualizar_Tipodocumento.html", context)


#Vista para eliminar un autor
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Tipodocumento, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('Tipodocumento')    
    return render(request, "Tipodocumento/eliminar_Tipodocumento.html", context)



class TipoDocumentoListApiView(APIView):

    def get(self,request,*args, **kwargs):
        '''
        Lista todos los tipo documentos en base de datos
        '''
        Tipodocumentos = Tipodocumento.objects.all()
        serializer = TipoDocumentoSerializer(Tipodocumentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request, *args, **kwargs):
        '''
        Crea un tipo documento en base de datos
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion'),
        }

        serializer = TipoDocumentoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipodocumentoDetailApiView(APIView):

    def get_object(self,Tipodocumento_id):
        '''
        Metodo de ayuda para retornar un tipo documento con un id Dado
        '''
        try:
            return Tipodocumento.objects.get(id=Tipodocumento_id)
        except Tipodocumento.DoesNotExist:
            return None
        
    def get(self,request,Tipodocumento_id, *args, **kwargs):
        '''
        Permite obtener un tipo documento por ID
        '''
        Tipodocumento_instance = self.get_object(Tipodocumento_id)
        if not Tipodocumento_instance:
            return Response(
                {"res":"El tipo documento con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        serializer = TipoDocumentoSerializer(Tipodocumento_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, Tipodocumento_id, *args, **kwargs):
        '''
        Actualiza un tipo documento por su ID
        '''
        Tipodocumento_instance = self.get_object(Tipodocumento_id)
        if not Tipodocumento_instance:
            return Response(
                {"res":"El tipo documento con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion')
        }

        serializer = TipoDocumentoSerializer(instance = Tipodocumento_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,Tipodocumento_id, *args, **kwargs):
        '''
        Elimina el tipo documento con el ID dado
        '''
        Tipodocumento_instance = self.get_object(Tipodocumento_id)
        if not Tipodocumento_instance:
            return Response(
                {"res":"El tipo documento con el id dado no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        Tipodocumento_instance.delete()
        return Response(
            {"res":"Object Deleted"},
            status=status.HTTP_200_OK
        )