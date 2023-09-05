from meal.models import Meal
from meal.serializers import MealSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def menuList(request):
    if request.method=='GET':
        meals=Meal.objects.all()
        meals_serializer=MealSerializer(meals,many=True)
        print(meals_serializer.data) 
        return JsonResponse({'message':"Menu Items",'error':False,'Payment':meals_serializer.data})
    
@api_view(['POST'])
def createNewMeal(request):
    meal_data=JSONParser().parse(request)
    meals_serializer=MealSerializer(data=meal_data)
    if meals_serializer.is_valid():
        meals_serializer.save()
        return JsonResponse({'message':'New Meal add Successfull','status':'200','error':False})
    return JsonResponse({'message':'fail to add new Meal','status':'404','error':True})

@api_view(['PUT'])
def updateExistingMeal(request,id):
    meal_data=JSONParser().parse(request)
    meal=Meal.objects.get(mealId=id)
    meals_serializer=MealSerializer(instance=meal,data=meal_data,partial=True)
    if meals_serializer.is_valid():
        meals_serializer.save()
        return JsonResponse({'message':'Meal Details updated Successfull','status':'200','error':False})
    return JsonResponse({'message':'Fail to update meal detail','status':'404','error':True})
    
@api_view(['DELETE'])
def deleteMeal(request, id):  # Note the parameter name 'id'
    try:
        meal = Meal.objects.get(mealId=id)
        meal.delete()
        return JsonResponse({'message': 'Meal Deleted Successfully', 'status': '200','error':False})
    except meal.DoesNotExist:
        return JsonResponse({'message': 'Meal not found', 'status': '404','error':True})





