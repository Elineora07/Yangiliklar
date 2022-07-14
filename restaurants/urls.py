from django.urls import path
from .views import RestaurantView


app_name = 'restaurant'
urlpatterns = [
    path('', RestaurantView.as_view(), name='index')
]
