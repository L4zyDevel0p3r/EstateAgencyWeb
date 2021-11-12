from utilities.validators import validate_image_size
from django.db.models.signals import pre_delete
from ckeditor.fields import RichTextField
from utilities.files import upload_file
from django.dispatch import receiver
from django.core import validators
from django.urls import reverse
from account.models import User
from django.db.models import Q
from django.db import models
from uuid import uuid4


# Create your models here.


def upload_image(instance, file):
    return upload_file(file, f"estate/{instance.advisor.username}")


def validate_img_size(image):
    validate_image_size(image, 2)


def generate_slug():
    return (str(uuid4()).split("-"))[0]


class EstateManager(models.Manager):
    def search(self, query):
        lookup = (
                Q(advisor__username__icontains=query) |
                Q(title__icontains=query) |
                Q(street__icontains=query) |
                Q(typ__icontains=query) |
                Q(address__icontains=query) |
                Q(description__icontains=query)
        )

        queryset = self.get_queryset().filter(lookup).distinct()

        return queryset


class Estate(models.Model):
    STATUS_CHOICES = [
        ("رهن", "رهن"),
        ("اجاره", "اجاره"),
        ("فروش", "فروش")
    ]

    IMAGE_FIELD_VALIDATORS = [
        validators.FileExtensionValidator(allowed_extensions=["PNG", "JPG", "JPEG"]),
        validate_img_size
    ]

    advisor = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="مشاور")
    title = models.CharField(max_length=50, verbose_name="عنوان")
    price = models.CharField(max_length=50, verbose_name="قیمت")
    street = models.CharField(max_length=20, verbose_name="خیابان")
    area = models.CharField(max_length=20, verbose_name="متراژ")
    typ = models.CharField(max_length=20, verbose_name="نوع ملک")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="وضعیت")
    room = models.PositiveSmallIntegerField(verbose_name="تعداد اتاق")
    parking = models.PositiveSmallIntegerField(verbose_name="تعداد پارکینگ")
    year_of_construction = models.PositiveSmallIntegerField(verbose_name="سال ساخت")
    address = models.CharField(max_length=50, verbose_name="آدرس")
    img1 = models.ImageField(upload_to=upload_image, verbose_name="تصویر 1", validators=IMAGE_FIELD_VALIDATORS)
    img2 = models.ImageField(upload_to=upload_image, verbose_name="تصویر 2", validators=IMAGE_FIELD_VALIDATORS)
    img3 = models.ImageField(upload_to=upload_image, verbose_name="تصویر 3", validators=IMAGE_FIELD_VALIDATORS)
    img4 = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر 4",
                             validators=IMAGE_FIELD_VALIDATORS)
    img5 = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر 5",
                             validators=IMAGE_FIELD_VALIDATORS)
    img6 = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر 6",
                             validators=IMAGE_FIELD_VALIDATORS)
    description = RichTextField(verbose_name="توضیحات")
    is_special_ad = models.BooleanField(default=False, verbose_name="آگهی ویژه")
    slug = models.SlugField(default=generate_slug, unique=True, editable=False, verbose_name="Slug")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")

    objects = EstateManager()

    def get_absolute_url(self):
        return reverse("EstateApp:estate_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "املاک"
        verbose_name = "ملک"


@receiver(signal=pre_delete, sender=Estate)
def estate_pre_delete_receiver(sender, instance, *args, **kwargs):
    image_list = [instance.img1, instance.img2, instance.img3, instance.img4, instance.img5, instance.img6]

    for img in image_list:
        if img:
            img.delete(save=False)
