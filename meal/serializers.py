from rest_framework import serializers
from meal.models import Meal
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields=('mealId','mealName','price','description','category','isAvailable')