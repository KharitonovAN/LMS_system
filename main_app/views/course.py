from rest_framework.viewsets import ModelViewSet
from main_app.models import Course
from main_app.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
