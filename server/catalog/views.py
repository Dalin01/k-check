from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRooms(request):
  return Response({'Rooms': 'yes'})

@api_view(['GET'])
def getRoom(request, pk):
  return Response({'pk': pk})