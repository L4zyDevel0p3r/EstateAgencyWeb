from django.views.generic import ListView
from contact.models import SocialNetwork
from django.shortcuts import render
from estate.models import Estate


class HomePage(ListView):
    template_name = "home.html"
    model = Estate
    ordering = "-date"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        special_ads = Estate.objects.filter(is_special_ad=True).order_by(self.ordering)

        context.update({
            "special_ads": special_ads
        })

        return context


def header(request, *args, **kwargs):
    context = {
        "reqpath": kwargs.get("reqpath")
    }

    return render(request, "shared/Header.html", context)


def footer(request):
    social_network = SocialNetwork.objects.last()

    context = {
        "social_network": social_network
    }

    return render(request, "shared/Footer.html", context)

# todo: piade sazi page darbare ma - ✅,
#  fix kardan link WhatsApp dar footer,
#  piade sazi bakhsh moshaver amlak dar estate detail,
#  piade sazi login/register - ✅,
#  ijad image size va extension validator baraye field logo user va image field haye estate,
#  taghir template admin.
