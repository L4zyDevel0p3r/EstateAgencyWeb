from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core import validators
from .models import User
from django import forms


class LoginForm(forms.Form):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'advisor_name', 'email', 'logo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].validators = [
            *self.fields["username"].validators,
            validators.MinLengthValidator(8, "نام کاربری نمی تواند کمتر از 8 حرف باشد."),
            validators.MaxLengthValidator(20, "نام کاربری نمی تواند بیشتر از 20 حرف باشد.")
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)

        if qs.exists():
            raise forms.ValidationError("این ایمیل قبلا ثبت نام شده است.")

        return email
