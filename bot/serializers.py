from rest_framework import serializers
from .models import Food, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Food
        fields = '__all__'
