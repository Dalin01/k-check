from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class RoomType(models.Model):
  name = models.CharField(max_length=100, help_text='Enter a room type (e.g. Single/Double etc')

  def __str__(self):
    return self.name

class Room(models.Model):
  createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='creator')
  roomType = models.OneToOneField(RoomType,
                                  help_text='Select a room type', 
                                  on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200)
  rating = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  numReviews = models.IntegerField(default=0)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.TextField(max_length=1000, null=True)
  category = models.CharField(max_length=200, null=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(null=True, blank=True)

  STATUS = (
    ('a', 'Available'),
    ('b', 'Booked'),
    ('m', 'Maintenance')
  )

  status = models.CharField(
    max_length=1,
    choices=STATUS,
    blank=True,
    default='m',
    help_text='Room availability'
  )

  guest = models.ForeignKey(User, on_delete=models.SET_NULL,
                            null=True, blank=True, related_name='guest')
  availableAt = models.DateField(null=True, blank=True)

  def __str__(self):
    return self.name

class RoomImage(models.Model):
  room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
  image = models.ImageField(null=True, blank=True)

  def __str__(self):
    return '{0} {1}'.format(self.room.name, self.image)
  
class Review(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
  rating = models.IntegerField(default=1)
  comment = models.TextField(null=True, help_text='Please provide some comments')
  createdAt = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '{1} ({0}, {2})'.format(str(self.rating), str(self.user.username), str(self.room.name))

class BookingCart(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  paymentMethod = models.CharField(max_length=200, help_text='Enter payment method')
  tax = models.DecimalField(max_digits=6, decimal_places=2)
  total = models.DecimalField(max_digits=6, decimal_places=2)
  isPaid = models.BooleanField(default=False)
  paidAt = models.DateTimeField(auto_now_add=False, null=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return str(self.createdAt)

class CartItem(models.Model):
  name = models.CharField(max_length=200, help_text='Enter a name for the Room')
  price = models.DecimalField(max_digits=6, decimal_places=2)
  room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)
  bookingCart = models.OneToOneField(BookingCart, on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.name

  
  

