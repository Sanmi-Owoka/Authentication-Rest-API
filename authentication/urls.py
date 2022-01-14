from django.urls import path
from .views.register import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
]
