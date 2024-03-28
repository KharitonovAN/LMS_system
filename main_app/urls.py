from django.urls import path
from main_app.apps import MainAppConfig
from rest_framework.routers import DefaultRouter
from main_app.views.course import CourseViewSet
from main_app.views.lesson import (
    LessonListAPIView,
    LessonCreateAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonDeleteAPIView
)


app_name = MainAppConfig.name


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [

    path('', LessonListAPIView.as_view(), name='lessons_list'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson_delete'),

] + router.urls
