from django.shortcuts import render
from Aeropuerto_App.models import *
from Aeropuerto_App.serializers import *
from rest_framework import viewsets,status
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
class Usuario_view(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_Serializer

class Avion_view(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = Avion_Serializer

class Piloto_view(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = Piloto_Serializer

class Tripulacion_view(viewsets.ModelViewSet):
    queryset = Tripulacion.objects.all()
    serializer_class = Tripulacion_Serializer

class Vuelo_view(viewsets.ModelViewSet):
    queryset = Vuelo.objects.all()
    serializer_class = Vuelo_Serializer

class Itinerario_view(viewsets.ModelViewSet):
    queryset = Itinerario.objects.all()
    serializer_class = Itinerario_Serializer   

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if(token):
            token.delete()
            token, created = Token.objects.get_or_create(user=user)
        
        user.token = token.key
        user.save()
        usuario = Usuario_Serializer(user)
        return Response(usuario.data)