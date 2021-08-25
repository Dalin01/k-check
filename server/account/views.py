from django.shortcuts import render
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Custom serializer token class to include user details.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):  
  def validate(self, attrs):
    data = super().validate(attrs)
    data['username'] = self.user.username
    data['email'] = self.user.email
    data['first_name'] = self.user.first_name
    data['last_name'] = self.user.last_name
    return data

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer


def login(request):
  return JsonResponse({'Hello': 'Hi'})