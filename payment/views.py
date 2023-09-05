from payment.models import Payment
from payment.serializers import PaymentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from reservation.models import Reservation
from reservation.serializers import ReservationSerializer

# Create your views here.

@api_view(['GET'])
def paymentsList(request):
    if request.method=='GET':
        payments=Payment.objects.all()
        print("Queryset: {payments}")
        payment_serializer=PaymentSerializer(payments,many=True)
        print(payment_serializer.data) 
        return JsonResponse({'message':"List of Payment Transaction",'error':False,'Payment':payment_serializer.data})
    
@api_view(['POST'])
def createPayment(request):
    payment_data=JSONParser().parse(request)
    payments_serializer=PaymentSerializer(data=payment_data)
    reservation = Reservation.objects.get(paymentTransactionToken=payment_data['paymentTransactionToken'])
    if payments_serializer.is_valid():
        instance=payments_serializer.save()
        data1 = {'paid': 'true'}
        reserveSerializer = ReservationSerializer(reservation, data=data1,partial=True)
        if reserveSerializer.is_valid():
            reserveSerializer.save()
        return JsonResponse({'message':'Payment done successfull','error':False,'paymentRecordId':instance.paymentId,'paymentTransactionToken':payment_data['paymentTransactionToken'],'status':'200'})
    return JsonResponse({'message':'Payment transaction fail try again','error':True,'status':'404'})
    

