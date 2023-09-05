from django.db import models

# Create your models here.
class Meal(models.Model):
    mealId=models.AutoField(primary_key=True)
    mealName=models.CharField(max_length=25)
    price=models.BigIntegerField()
    description=models.CharField(max_length=25)
    category=models.CharField(max_length=25)
    isAvailable=models.IntegerField()