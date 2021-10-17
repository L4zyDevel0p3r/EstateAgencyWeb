from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("فیلد های اضافه", {"fields": ("advisor_name", "phone", "mobile", "address", "logo")}),
    )

    class Meta:
        model = User
