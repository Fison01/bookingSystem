from django.shortcuts import render
from user.models import User
from rest_framework import status
from user.serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def userList(request):
    if request.method=='GET':
        users=User.objects.all()
        users_serializer=UserSerializer(users,many=True)
        print(users_serializer.data) 
        return Response(users_serializer.data)
    
@api_view(['POST'])
def createUser(request):
    user_data=JSONParser().parse(request)
    users_serializer=UserSerializer(data=user_data)
    if users_serializer.is_valid():
        users_serializer.save()
        return JsonResponse({'message':'Client Successfull record','status':'200'})
    return JsonResponse({'message':'fail to add new Client','status':'404'})

@api_view(['PUT'])
def updateUser(request,id):
    user_data=JSONParser().parse(request)
    user=User.objects.get(userId=id)
    users_serializer=UserSerializer(instance=user,data=user_data)
    if users_serializer.is_valid():
        users_serializer.save()
        return JsonResponse({'message':'Client Details updated Successfull','status':'200'})
    return JsonResponse({'message':'fail to update Client detail','status':'404'})
    
@api_view(['DELETE'])
def deleteUser(request, id):  # Note the parameter name 'id'
    try:
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse({'message': 'Client deleted Successfully', 'status': '200'})
    except User.DoesNotExist:
        return JsonResponse({'message': 'Client not found', 'status': '404'})

