from django.core import validators
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg form-control-a", "placeholder": "نام بنگاه"}
        ),
        validators=[
            validators.MinLengthValidator(4, "طول این قسمت نمی تواند کمتر از 4 حرف باشد."),
            validators.MaxLengthValidator(50, "طول این قسمت نمی تواند بیشتر از 50 حرف باشد.")
        ]
    )

    consultant_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg form-control-a", "placeholder": "نام مشاور"}
        ),
        validators=[
            validators.MinLengthValidator(4, "طول این قسمت نمی تواند کمتر از 4 حرف باشد."),
            validators.MaxLengthValidator(20, "طول این قسمت نمی تواند بیشتر از 20 حرف باشد.")
        ]
    )

    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={"class": "form-control form-control-lg form-control-a", "placeholder": "شماره تماس"}
        ),
        validators=[
            validators.MinLengthValidator(8, "طول این قسمت نمی تواند کمتر از 8 رقم باشد."),
            validators.MaxLengthValidator(20, "طول این قسمت نمی تواند بیشتر از 20 رقم باشد.")
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "آدرس بنگاه و توضیحات بیشتر", "cols": "45", "rows": "8"}
        ),
        validators=[
            validators.MinLengthValidator(10, "طول این قسمت نمی تواند کمتر از 10 حرف باشد.")
        ]
    )
