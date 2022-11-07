import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from base.api.serializers import IncubationSerializer, RegisterSerializer, SlotSerializer
from django.contrib.auth.models import User

from base.models import Incubation, Slot


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
  users = User.objects.filter(is_superuser=False)
  serializer = RegisterSerializer(users, many=True)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getIncubations(request):
  incubations = Incubation.objects.all()
  serializer = IncubationSerializer(incubations, many=True)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getIndividualIncubation(request, id):
  incubation = Incubation.objects.get(id=id)
  serializer = IncubationSerializer(incubation)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getNewIncubations(request):
  incubations = Incubation.objects.filter(is_new=True)
  serializer = IncubationSerializer(incubations, many=True)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getPendingIncubations(request):
  incubations = Incubation.objects.filter(is_new=False, is_declined=False, is_slot_allotted=False)
  serializer = IncubationSerializer(incubations, many=True)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getWaitingIncubations(request):
  incubations = Incubation.objects.filter(is_approved=True, is_slot_allotted=False)
  serializer = IncubationSerializer(incubations, many=True)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def setIncubationsPending(request, id):
  incubation = Incubation.objects.get(id=id)
  incubation.is_new=False
  incubation.save()
  serializer = IncubationSerializer(incubation)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def setIncubationsApprove(request, id):
  incubation = Incubation.objects.get(id=id)
  incubation.is_approved=True
  incubation.is_declined=False
  incubation.save()
  serializer = IncubationSerializer(incubation)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def setIncubationsDeclined(request, id):
  incubation = Incubation.objects.get(id=id)
  incubation.is_declined=True
  incubation.is_approved=False
  incubation.save()
  serializer = IncubationSerializer(incubation)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAllSlots(request):
  slots = Slot.objects.all()
  serializer = SlotSerializer(slots, many=True)
  return Response(serializer.data)

  

@api_view(['GET'])
@permission_classes([IsAdminUser])
def slotAllocate(request, application_id, slot_id):
  slot = Slot.objects.get(id=slot_id)
  incubation = Incubation.objects.get(id=application_id)
  slot.company = incubation
  slot.save()
  incubation.is_slot_allotted=True
  incubation.save()
  serializer = SlotSerializer(slot)
  return Response(serializer.data)


  