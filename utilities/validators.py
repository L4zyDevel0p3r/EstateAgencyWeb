from django.core.validators import ValidationError


def validate_image_size(image, limit_mb):
    if image.size > limit_mb * 1024 * 1024:
        raise ValidationError("حجم فایل از حد مجاز (%s مگابایت) بیشتر است." % limit_mb)
