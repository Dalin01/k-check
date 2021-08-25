from django.contrib import admin
from .models import Room, RoomType, Review, BookingCart, CartItem, RoomImage

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Review)
admin.site.register(BookingCart)
admin.site.register(CartItem)
admin.site.register(RoomImage)
