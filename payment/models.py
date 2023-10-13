from django.db import models

# Create your models here.
class Payment(models.Model):
    paymentId=models.AutoField(primary_key=True)
    paymentTransactionToken=models.CharField(max_length=250)
    debutCardNo=models.CharField(max_length=25)
    cardHolderNames=models.CharField(max_length=25)
    expiredDate=models.CharField(max_length=25)
    cvvCode=models.CharField(max_length=25)
    amount=models.BigIntegerField()