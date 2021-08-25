from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  *
from .serializer import *

@api_view(['GET'])
def rooms_view(request):
  rooms = Room.objects.all()
  return Response(RoomSerializer(rooms, many=True).data)

@api_view(['GET'])
def room_detail_view(request, pk):
  return Response({'pk': pk})