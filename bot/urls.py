from django.urls import path
from . import views


urlpatterns = [
    path('food/', views.FoodsAPIView.as_view())
]