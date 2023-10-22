from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['city'] = instance.city.city_name
        return representation


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=100)

    class Meta:
        model = Shop
        fields = '__all__'

    def create(self, validated_data):
        city_name = validated_data.pop('city')
        street_name = validated_data.pop('street')

        try:
            city = City.objects.get(city_name=city_name)
        except City.DoesNotExist:
            raise ValidationError({"error": "Такого города нет в базе данных"})

        try:
            street = Street.objects.get(street_name=street_name,
                                        city__city_name=city_name)
        except Street.DoesNotExist:
            raise ValidationError({"error": "Такой улицы нет в базе данных"})

        validated_data['city'] = city
        validated_data['street'] = street

        return super().create(validated_data)
