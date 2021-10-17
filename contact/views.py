from .models import Support, ContactUs
from django.shortcuts import render
from .forms import ContactForm


# Create your views here.


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    support = Support.objects.last()

    context = {
        "support": support,
        "contact_form": contact_form,
        "success": False
    }

    if contact_form.is_valid():
        name = contact_form.cleaned_data.get("name")
        consultant_name = contact_form.cleaned_data.get("consultant_name")
        phone = contact_form.cleaned_data.get("phone")
        text = contact_form.cleaned_data.get("text")

        ContactUs.objects.create(name=name, consultant_name=consultant_name, phone=phone, text=text)

        context["contact_form"] = ContactForm()
        context["success"] = True

    return render(request, "contact_us.html", context)
