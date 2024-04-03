from users.models import User
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from users.serializers.user import UserSerializer, UserProfileSerializer


class UserUpdateAPIView(UpdateAPIView):
    """Представление для обновления User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProfileAPIView(RetrieveAPIView):
    """Представление для User"""
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
