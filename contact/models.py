from django.db import models


# Create your models here.


class Support(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.SmallIntegerField(verbose_name="شماره تماس")

    class Meta:
        verbose_name_plural = "پشتیبانی"
        verbose_name = "پشتیبانی"

    def __str__(self):
        return self.email


class SocialNetwork(models.Model):
    whatsapp = models.CharField(max_length=25, verbose_name="واتس‌اپ")
    instagram = models.CharField(max_length=25, verbose_name="اینستاگرام")

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"


class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام بنگاه")
    consultant_name = models.CharField(max_length=20, verbose_name="نام مشاور")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    text = models.TextField(verbose_name="آدرس بنگاه و توضیحات بیشتر")
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاریخ")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده")

    class Meta:
        verbose_name_plural = "تماس ها"
        verbose_name = "تماس"

    def __str__(self):
        return self.name
