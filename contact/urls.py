from .views import contact_page
from django.urls import path

app_name = 'ContactApp'

urlpatterns = [
    path('contact', contact_page, name="ContactUs")
]
