from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from utilities.files import upload_file
from django.dispatch import receiver
from django.db import models


# Create your models here.

def upload_logo(instance, file):
    return upload_file(file, f"logo/{instance.username}")


class User(AbstractUser):
    advisor_name = models.CharField(max_length=25, null=True, verbose_name="نام مشاور")
    logo = models.ImageField(upload_to=upload_logo, null=True, verbose_name="لوگوی بنگاه")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="تلفن")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="همراه")
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name="آدرس")

    def save(self, *args, **kwargs):
        try:
            this = User.objects.get(pk=self.pk)
            if this.logo != self.logo:
                this.logo.delete(save=False)
        except:
            pass

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "حساب ها"
        verbose_name = "حساب"
        db_table = 'auth_user'


@receiver(signal=pre_delete, sender=User)
def user_pre_delete_receiver(sender, instance, *args, **kwargs):
    instance.logo.delete(save=False)
