from urllib import response
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User

from base.models import Incubation
from .serializers import IncubationSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['admin'] = user.is_superuser

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class IncubationView(generics.CreateAPIView):
    queryset = Incubation.objects.all()
    # parser_classes = (MultiPartParser, FormParser)
    serializer_class = IncubationSerializer


@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/token',
    '/api/token/refresh',
  ]

  return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getIncubation(request):
  user = request.user
  incubations = Incubation.objects.filter(user=user)
  serializer = IncubationSerializer(incubations, many=True)
  return Response(serializer.data)