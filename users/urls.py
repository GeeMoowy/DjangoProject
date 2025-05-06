from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from .views import UserRegistrationForm

app_name = UsersConfig.name

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), ),
]