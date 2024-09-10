from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Review
from .serializers import ReviewSerializer

# class ReviewListCreate(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     parser_classes = [MultiPartParser, FormParser]  # Добавляем поддержку загрузки файлов

#     def perform_create(self, serializer):
#         serializer.save()

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset

#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         average_rating = self.get_queryset().aggregate(average=Avg('rating'))['average']
#         response.data = {
#             'average_rating': average_rating,
#             'ratings_count': self.get_queryset().count(),
#             'ratings': response.data
#         }
#         return response

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser  # Для поддержки загрузки файлов
from django.db.models import Avg  # Для расчета среднего значения рейтинга


class ReviewListCreate(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    parser_classes = [MultiPartParser, FormParser]  # Добавляем парсеры для поддержки загрузки файлов

    def perform_create(self, serializer):
        # Сохранение нового объекта
        serializer.save()

    def get_queryset(self):
        # Получаем базовый набор данных
        queryset = super().get_queryset()
        return queryset

    def list(self, request, *args, **kwargs):
        # Вызываем стандартный метод для получения списка объектов
        response = super().list(request, *args, **kwargs)

        # Рассчитываем средний рейтинг
        average_rating = self.get_queryset().aggregate(average=Avg('rating'))['average']

        # Модифицируем ответ, добавляя информацию о среднем рейтинге и количестве оценок
        response.data = {
            'average_rating': average_rating,
            'ratings_count': self.get_queryset().count(),
            'ratings': response.data
        }

        return response
