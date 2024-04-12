from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User
from users.permissions import IsUserOwner
from users.serializers.user import (
    UserSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer
)
from rest_framework.generics import (
    UpdateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    ListAPIView, DestroyAPIView
)


class UserUpdateAPIView(UpdateAPIView):
    """Представление для обновления User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]


class UserProfileAPIView(RetrieveAPIView):
    """Представление для User"""
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]


class UserRegistrationAPIView(CreateAPIView):
    """Представление для регистрации User"""
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data['password'])  # Зашифрованный пароль
            user.is_active = True  # Активирование пользователя
            user.groups.add(Group.objects.get(name='MEMBER'))  # Добавление пользователя в группу
            user.save()
        return Response({'message': 'User создан успешно.'})


class UserListAPIView(ListAPIView):
    """Представление для отображения списка Users"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDeleteAPIView(DestroyAPIView):
    """Представление для удаления User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
