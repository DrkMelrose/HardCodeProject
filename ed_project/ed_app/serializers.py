from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    #is_viewed = serializers.BooleanField()

    class Meta:
        model = Lesson
        fields = '__all__'


class ProductStatsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField()
    total_viewed_lessons = serializers.IntegerField()
    total_viewed_time_seconds = serializers.IntegerField()
    total_students = serializers.IntegerField()
    acquisition_percentage = serializers.FloatField()