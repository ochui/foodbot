from rest_framework import generics
from rest_framework import filters

from .models import Food, Ingredient
from .serializers import FoodSerializer


class FoodsAPIView(generics.ListCreateAPIView):

    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
