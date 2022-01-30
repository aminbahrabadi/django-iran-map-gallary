from django.db import models

from .validators import image_field_validator
from .file_names import stats_image_upload_to


class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False, verbose_name='نام')
    number_of_trees = models.PositiveIntegerField(default=0, verbose_name='تعداد درخت ها')
    css_id = models.CharField(max_length=155, null=True, blank=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name


class Image(models.Model):
    state = models.ForeignKey(State, null=True, blank=False,
                              verbose_name='استان', on_delete=models.CASCADE, related_name='images')
    file = models.FileField(validators=[image_field_validator],
                            upload_to=stats_image_upload_to,
                            null=True,
                            blank=True,
                            verbose_name='فایل تصویر')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')

    def __str__(self):
        return '{}'.format(self.id)
