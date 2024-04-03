from main_app.models import Lesson
from main_app.serializers.lesson import LessonSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)


class LessonListAPIView(ListAPIView):
    """Представление для просмотра всех объектов"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    """Представление для создания нового объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    """"Представление для обновления объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    """Представление для деталей одного объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(DestroyAPIView):
    """Представление для удаления объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
