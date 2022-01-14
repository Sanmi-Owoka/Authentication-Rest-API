from django.urls import path
from .views.register import RegisterView
from .views.email_verification import VerifyEmail
from .views.login import LoginView
from .views.logout import LogoutView
from .views.forgot_password import ForgotPasswordView
from .views.reset_password import PasswordResetView
urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('verify-email', VerifyEmail.as_view(), name='verify-email'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    path('password-reset', PasswordResetView.as_view(), name='password-reset'),
]
