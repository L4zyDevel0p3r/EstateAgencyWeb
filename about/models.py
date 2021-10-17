from ckeditor.fields import RichTextField
from utilities.files import upload_file
from django.db import models


# Create your models here.

def upload_image(instance, file):
    return upload_file(file, "about_us")


class AboutUs(models.Model):
    title = models.CharField(max_length=30, verbose_name="عنوان")
    image = models.ImageField(upload_to=upload_image, verbose_name="تصویر")
    description = RichTextField(verbose_name="توضیحات")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"
