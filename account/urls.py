from .views import LoginPage, RegisterPage
from django.urls import path

app_name = "AccountApp"

urlpatterns = [
    path('login', LoginPage.as_view(), name='Login'),
    path('register', RegisterPage.as_view(), name='Register')
]
