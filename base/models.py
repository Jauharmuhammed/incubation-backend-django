from email.policy import default
from enum import unique
from pyexpat import model
from random import choices
from secrets import choice
from venv import create
from django.db import models
from django.contrib.auth.models import User


class Incubation(models.Model):
  types_of_incubation = (
    ('Physical Incubation','Physical Incubation'),
    ('Virtual Incubation','Virtual Incubation')
  )
  
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  is_new = models.BooleanField(default=True)
  is_approved = models.BooleanField(default=False)
  is_declined = models.BooleanField(default=False)
  is_slot_allotted = models.BooleanField(default=False)

  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  email = models.EmailField(max_length=100)
  phone_number = models.CharField(max_length=255)
  company_name = models.CharField(max_length=255)
  company_logo = models.ImageField(upload_to='images/company_logos', blank=True, null=True)

  team_and_background = models.TextField()
  company_and_products = models.TextField()
  problem_to_solve = models.TextField()
  solution = models.TextField()
  value_proposition_for_customer = models.TextField()
  competetors = models.TextField()
  revenue_model = models.TextField()
  market_size = models.TextField()
  market_plan = models.TextField()
  type_of_incubation = models.CharField(choices=types_of_incubation, max_length= 100)
  business_proposal = models.TextField()

  def __str__(self):
    return self.company_name



class Slot(models.Model):
  company = models.OneToOneField(Incubation, on_delete=models.CASCADE, blank=True, null=True)
  create_date = models.DateTimeField(auto_now_add=True)


  def company_name(self):
    if self.company:
      return self.company.company_name