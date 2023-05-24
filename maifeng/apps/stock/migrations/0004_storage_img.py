# Generated by Django 3.0 on 2022-03-30 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20220301_1428'),
        ('stock', '0003_auto_20220220_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='img',
            field=models.ForeignKey(blank=True, help_text='图片（ForeignKey）', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='storage_img', to='files.Images', verbose_name='图片'),
        ),
    ]