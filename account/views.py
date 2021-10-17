from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from .forms import LoginForm, RegisterForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy


# Create your views here.


class LoginPage(FormView):
    form_class = LoginForm
    success_url = reverse_lazy("HomePage")
    template_name = "auth/login.html"

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy("HomePage"))

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)

        if user is None:
            form.add_error("password", "کاربری با مشخصات وارد شده وجود ندارد.")

        else:
            login(self.request, user)
            return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(form=form))


class RegisterPage(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy("AccountApp:Login")
    template_name = "auth/register.html"

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy("HomePage"))

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())
