from django.views.generic import ListView, DetailView
from .models import Estate


# Create your views here.


class EstateList(ListView):
    model = Estate
    paginate_by = 6
    ordering = "-date"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_by = self.request.GET.get("filter_by")
        q = self.request.GET.get("q")

        if q:
            ordering = self.get_ordering()
            queryset = self.model.objects.search(query=q).order_by(ordering)

        if filter_by == "oldest":
            queryset = queryset.order_by("date")

        elif filter_by == "rent":
            queryset = queryset.filter(status="اجاره")

        elif filter_by == "mortgage":
            queryset = queryset.filter(status="رهن")

        elif filter_by == "sale":
            queryset = queryset.filter(status="فروش")

        return queryset


class EstateListSpecial(EstateList):
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(is_special_ad=True)

        return queryset


class EstateDetail(DetailView):
    model = Estate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context.get("object")
        # Yek list az image hayi ke object dare misazim
        obj_image_list = [obj.img1, obj.img2, obj.img3, obj.img4, obj.img5, obj.img6]

        context.update({
            # Yek list az image hayi ke toye obj_image_list hastan misazim ke meghdareshon None nabashe
            # va be context ezafe mikonim.
            "object_image_list": [img for img in obj_image_list if img]
        })

        return context
