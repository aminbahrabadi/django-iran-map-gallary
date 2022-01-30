# Generated by Django 4.0.1 on 2022-01-25 11:05

from django.db import migrations, models
import django.db.models.deletion
import stats.file_names
import stats.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='نام')),
                ('number_of_trees', models.PositiveIntegerField(default=0, verbose_name='تعداد درخت ها')),
                ('css_id', models.CharField(blank=True, max_length=155, null=True)),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=stats.file_names.stats_image_upload_to, validators=[stats.validators.image_field_validator], verbose_name='فایل تصویر')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.state', verbose_name='استان')),
            ],
        ),
    ]
