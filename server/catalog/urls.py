from django.urls import path
from . import views

urlpatterns = [
  path('rooms/', views.getRooms, name='rooms'),
  path('room/<int:pk>/', views.getRoom, name='room'),
]
