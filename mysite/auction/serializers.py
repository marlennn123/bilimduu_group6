from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'