from reservation.models import Reservation
from reservation.serializers import ReservationSerializer
from reservation.models import Reservation
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
# Create your views here.

@api_view(['GET'])
def roomReservations(request):
    if request.method=='GET':
        rooms=Reservation.objects.select_related('bookedRoomId','personId').all()
        rooms_serializer=ReservationSerializer(rooms,many=True)
        return JsonResponse({'message':"Room Reservation Transaction",'error':False,'payment':rooms_serializer.data})
    
@api_view(['POST'])
def createRoomReservation(request):
    room_data=JSONParser().parse(request)
    rooms_serializer=ReservationSerializer(data=room_data)
    if rooms_serializer.is_valid():
        instance=rooms_serializer.save()
        return JsonResponse({'message':'Room reserved successfull','Next steps':'Your payment must be made no later than tomorrow at noon.','paymentTransactionToken':instance.paymentTransactionToken,'status':'200','error':False})
    return JsonResponse({'message':'fail to reserve room','status':'300','error':True})

@api_view(['PUT'])
def updateRoomReservation(request,id):
    room_data=JSONParser().parse(request)
    room=Reservation.objects.get(roomId=id)
    rooms_serializer=ReservationSerializer(instance=room,data=room_data)
    if rooms_serializer.is_valid():
        rooms_serializer.save()
        return JsonResponse({'message':'updated Successfull','status':'200','error':False})
    return JsonResponse({'message':'fail to update room detail','status':'300','error':False})
    
@api_view(['DELETE'])
def deleteRoomReservation(request, id):  # Note the parameter name 'id'
    try:
        room = Reservation.objects.get(bookingId=id)
        room.delete()
        return JsonResponse({'message': 'deleted Successfully', 'status': '200','error':False})
    except Reservation.DoesNotExist:
        return JsonResponse({'message': 'Room reservation not found', 'status': '404','error':True})
    

