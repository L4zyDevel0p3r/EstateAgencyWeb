from .models import Support, SocialNetwork, ContactUs
from django.contrib import admin


# Register your models here.

@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ("__str__", "phone")

    class Meta:
        model = Support


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("whatsapp", "instagram")

    class Meta:
        model = SocialNetwork


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("__str__", "phone", "date", "is_read")
    list_editable = ("is_read",)
    list_filter = ("is_read", "date")

    class Meta:
        model = ContactUs
