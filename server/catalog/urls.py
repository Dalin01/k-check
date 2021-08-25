from django.urls import path
from . import views

urlpatterns = [
  path('rooms/', views.rooms_view, name='rooms'),
  path('room/<int:pk>/', views.room_detail_view, name='room-detail'),
]
