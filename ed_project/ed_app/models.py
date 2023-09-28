from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MyModels(models.Model):
    time_now = models.DateTimeField(default=timezone.now)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time_seconds = models.PositiveIntegerField(default=0)
    is_viewed = models.BooleanField(default=False)
    last_viewed_at = models.DateTimeField(null=True, blank=True)



