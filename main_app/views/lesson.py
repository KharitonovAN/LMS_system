from rest_framework.permissions import IsAuthenticated

from main_app.models import Lesson
from main_app.permissions import IsModerator, IsOwner
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
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(CreateAPIView):
    """Представление для создания нового объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user  # владелец
        new_lesson.save()


class LessonUpdateAPIView(UpdateAPIView):
    """"Представление для обновления объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonRetrieveAPIView(RetrieveAPIView):
    """Представление для деталей одного объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteAPIView(DestroyAPIView):
    """Представление для удаления объекта"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
