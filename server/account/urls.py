from django.urls import path
from . import views

urlpatterns = [
  path('', views.login, name='login'),
  path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
