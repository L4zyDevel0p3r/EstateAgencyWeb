from .views import AboutUsPage
from django.urls import path

app_name = "AboutUsApp"

urlpatterns = [
    path("about_us", AboutUsPage.as_view(), name="about_us")
]
