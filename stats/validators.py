from django.core.exceptions import ValidationError


def image_field_validator(image):
    allowed_extensions = ['jpg', 'png', 'jpeg']
    image_extension = image.name.split('.')[-1]

    if image_extension not in allowed_extensions:
        raise ValidationError('لطفا تصویر با '
                              'فرمت {} وارد کنید'.format(' | '.join(allowed_extensions)))
