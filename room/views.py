from room.models import Room
from room.serializers import RoomSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def roomApi(request):
    if request.method=='GET':
        rooms=Room.objects.all()
        rooms_serializer=RoomSerializer(rooms,many=True)
        print(rooms_serializer.data) 
        return JsonResponse({'message':"List Of Rooms",'error':False,'Rooms List':rooms_serializer.data})
    
@api_view(['POST'])
def createRoom(request):
    room_data=JSONParser().parse(request)
    rooms_serializer=RoomSerializer(data=room_data)
    if rooms_serializer.is_valid():
        rooms_serializer.save()
        return JsonResponse({'message':'Add Successfull','status':'200','error':False})
    return JsonResponse({'message':'fail to add new room','status':'404','error':True})

@api_view(['PUT'])
def updateRoom(request,id):
    room_data=JSONParser().parse(request)
    room=Room.objects.get(roomId=id)
    rooms_serializer=RoomSerializer(instance=room,data=room_data)
    if rooms_serializer.is_valid():
        rooms_serializer.save()
        return JsonResponse({'message':'Room Details updated Successfull','status':'200','error':False})
    return JsonResponse({'message':'Fail to update room detail','status':'404','error':True})
    
@api_view(['DELETE'])
def deleteRoom(request, id):  # Note the parameter name 'id'
    try:
        room = Room.objects.get(roomId=id)
        room.delete()
        return JsonResponse({'message': 'Room Deleted Successfully', 'status': '200','error':False})
    except Room.DoesNotExist:
        return JsonResponse({'message': 'Room not found', 'status': '404','error':True})
    
