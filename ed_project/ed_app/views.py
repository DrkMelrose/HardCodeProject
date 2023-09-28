from django.forms import BooleanField
from django.db.models import BooleanField
from rest_framework import generics
from .models import LessonView, Lesson, Product
from .serializers import LessonSerializer, ProductStatsSerializer
from django.shortcuts import render
from django.db.models import Count, Sum, Case, When, IntegerField, F
from django.contrib.auth.models import User


def home(request):
    return render(request, 'ed_app/home.html')


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user

        queryset = Lesson.objects.all()

        queryset = queryset.annotate(
            total_views=Count(
                Case(
                    When(lessonview__user=user, lessonview__is_viewed=True, then=1),
                    output_field=IntegerField(),
                ),
                distinct=True,
            )
        )

        queryset = queryset.annotate(
            total_viewed_time=Sum(
                Case(
                    When(
                        lessonview__user=user, lessonview__is_viewed=True, then=F('lessonview__viewed_time_seconds')
                    ),
                    default=0,
                    output_field=IntegerField(),
                ),
                distinct=True,
            )
        )

        return queryset


class LessonByProductAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        queryset = Lesson.objects.filter(products__id=product_id)
        queryset = queryset.annotate(
            is_viewed=Case(
                When(lessonview__user=user, lessonview__is_viewed=True, then=True),
                default=False,
                output_field=BooleanField(),
            ),
            viewed_time_seconds=Case(
                When(
                    lessonview__user=user, lessonview__is_viewed=True,
                    then=F('lessonview__viewed_time_seconds')
                ),
                default=0,
                output_field=IntegerField(),
            )
        )
        return queryset



class ProductStatsAPIView(generics.ListAPIView):
    serializer_class = ProductStatsSerializer

    def get_queryset(self):
        products = Product.objects.all()
        product_stats = []
        total_users = User.objects.count()
        for product in products:
            total_viewed_lessons = LessonView.objects.filter(
                lesson__products=product, is_viewed=True
            ).count()

            total_viewed_time_seconds = LessonView.objects.filter(
                lesson__products=product, is_viewed=True
            ).aggregate(Sum('viewed_time_seconds'))['viewed_time_seconds__sum'] or 0

            total_students = User.objects.filter(lessons__products=product).distinct().count()

            access_count = product.access_set.count()

            acquisition_percentage = (access_count / total_users) * 100 if total_users > 0 else 0

            product_stat = {
                'product_name': product.name,
                'total_viewed_lessons': total_viewed_lessons,
                'total_viewed_time_seconds': total_viewed_time_seconds,
                'total_students': total_students,
                'acquisition_percentage': acquisition_percentage,
            }

            product_stats.append(product_stat)

        return product_stats



