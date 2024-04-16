from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'category', 'marka', 'model', 'name', 'price', 'year', 'mileage', 'city', 'country',
                  'with_photo', 'color', 'volume', 'description']


class BetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()  # Поле user будет обработано с использованием метода get_user
    car = serializers.SerializerMethodField()   # Поле car будет обработано с использованием метода get_car

    class Meta:
        model = Bet
        fields = '__all__'  # Замените 'amount' на поля, которые вы хотите включить в сериализацию

    def get_user(self, instance):
        user_instance = instance.user
        return user_instance.username

    def get_car(self, instance):
        car_instance = instance.car
        return car_instance.name
