from django.db import models

# Create your models here.
class Room(models.Model):
    roomId=models.AutoField(primary_key=True)
    roomtype=models.CharField(max_length=25)
    roomNo=models.CharField(max_length=25)
    aminities=models.CharField(max_length=25)
    price=models.BigIntegerField()
    isAvailable=models.IntegerField()