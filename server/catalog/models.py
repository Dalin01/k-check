from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, help_text='Enter a name for the Room')
  rating = models.DecimalField(max_digits=6, decimal_places=2, null=True)
  numReviews = models.IntegerField(default=0)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.TextField(null=True, help_text='Provide some description for the room')
  category = models.CharField(max_length=200, help_text='Enter a Room category', null=True)
  createdAt = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
      return self.name
  

