from django.db import models

# Create your models here.
class User(models.Model):
    userId=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=25)
    phoneNo=models.CharField(max_length=25)
    nationality=models.CharField(max_length=25)
    idNo=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
