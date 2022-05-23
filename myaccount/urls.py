from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginView.as_view()),
    path('activation/', views.ActivationView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('users/', views.UserListAPIView.as_view()),
]



















































































