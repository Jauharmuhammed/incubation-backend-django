from django.urls import path
from . import views


urlpatterns = [
  path('users/all/', views.getUsers ),

  path('incubations/all/', views.getIncubations ),
  path('incubations/<int:id>/', views.getIndividualIncubation ),
  path('incubations/new/', views.getNewIncubations ),
  path('incubations/pending/', views.getPendingIncubations ),
  path('incubations/waiting/', views.getWaitingIncubations ),

  path('incubations/pending/<int:id>/', views.setIncubationsPending ),
  path('incubations/approve/<int:id>/', views.setIncubationsApprove ),
  path('incubations/decline/<int:id>/', views.setIncubationsDeclined ),

  path('slots/all/', views.getAllSlots ),
  path('slot-allocate/<int:application_id>/<int:slot_id>/', views.slotAllocate ),

]