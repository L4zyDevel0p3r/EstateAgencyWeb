from django.views.generic import TemplateView
from .models import AboutUs


# Create your views here.


class AboutUsPage(TemplateView):
    template_name = "about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_us = AboutUs.objects.last()

        context.update({
            "about_us": about_us
        })

        return context
