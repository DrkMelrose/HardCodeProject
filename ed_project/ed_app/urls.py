from django.urls import path
from .views import *





urlpatterns = [
    path('', home, name='home'),
    path('api/lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('api/product/<int:product_id>/lessons/', LessonByProductAPIView.as_view(), name='product-lessons'),
    path('api/product/stats/', ProductStatsAPIView.as_view(), name='product-stats')
]

