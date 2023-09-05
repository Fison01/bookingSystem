from rest_framework import serializers
from payment.models import Payment
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=('paymentId','paymentTransactionToken','debutCardno','cardHolderNames','expiredDate','cvvcode','amount')