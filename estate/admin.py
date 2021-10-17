from django.contrib import admin
from .models import Estate


# Register your models here.


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ("__str__", "typ", "date", "is_special_ad")
    list_filter = ("status", "is_special_ad", "date")

    class Meta:
        model = Estate
