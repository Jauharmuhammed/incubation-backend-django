from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  path('', views.getRoutes),
  path('incubation/data/', views.getIncubation ),

  path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('register/', views.RegisterView.as_view(), name='auth_register'),
  path('incubation/', views.IncubationView.as_view(), name='incubation'),
]