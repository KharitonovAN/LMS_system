from django.urls import path
from rest_framework.generics import DestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views.payment import PaymentListAPIView
from users.views.user import (
    UserUpdateAPIView,
    UserProfileAPIView,
    UserRegistrationAPIView,
    UserListAPIView
)

app_name = UsersConfig.name


urlpatterns = [

    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_profile_update'),
    path('<int:pk>/profile/', UserProfileAPIView.as_view(), name='user_profile'),
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
    path('registr/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('all/', UserListAPIView.as_view(), name='all_users'),
    path('delete/<int:pk>/', DestroyAPIView.as_view(), name='delete_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
