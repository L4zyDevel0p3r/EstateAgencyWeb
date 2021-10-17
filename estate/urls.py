from .views import EstateList, EstateListSpecial, EstateDetail
from django.urls import path

app_name = "EstateApp"

urlpatterns = [
    path("estate", EstateList.as_view(), name="estate_list"),
    path("estate_special", EstateListSpecial.as_view(), name="estate_list_special"),
    path("estate/<slug>", EstateDetail.as_view(), name="estate_detail")
]
