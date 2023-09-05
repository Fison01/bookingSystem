from rest_framework import serializers
from user.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('userId','firstName','lastName','phoneNo','idNo','nationality','address','email')