from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
  path('', views.login, name='login'), 
  path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
