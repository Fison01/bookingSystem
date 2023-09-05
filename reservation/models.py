from django.db import models
from room.models import Room
from user.models import User
from uuid import uuid4
# Create your models here.
class Reservation(models.Model):
    bookingId=models.AutoField(primary_key=True)
    bookedRoomId=models.ForeignKey(Room, on_delete=models.CASCADE)
    personId=models.ForeignKey(User, on_delete=models.CASCADE)
    checkInDate=models.CharField(max_length=25)
    checkOutDate=models.CharField(max_length=25)
    bookingDate=models.CharField(max_length=25)
    paymentTransactionToken=models.UUIDField(primary_key=False, default=uuid4, editable=False)
    paid=models.CharField(max_length=25)