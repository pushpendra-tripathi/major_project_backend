from django.urls import path
from .views import LoginView, RegisterView, ChangePassword, UpdateUserName, EmailVerification, ProfileView, PasswordReset



urlpatterns = [
    path("login/" , LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('changepassword/', ChangePassword.as_view()),
    path('updateusername/', UpdateUserName.as_view()),
    path('emailverify/', EmailVerification.as_view() ),
    path('profile/', ProfileView.as_view()),
    path('password/reset/', PasswordReset.as_view()),
]