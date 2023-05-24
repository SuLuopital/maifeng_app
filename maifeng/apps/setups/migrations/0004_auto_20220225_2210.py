# Generated by Django 3.0 on 2022-02-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0003_auto_20220225_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sysimages',
            options={'ordering': ['id'], 'verbose_name': '系统配置', 'verbose_name_plural': '系统配置'},
        ),
        migrations.AlterField(
            model_name='sysimages',
            name='with_models',
            field=models.CharField(choices=[('page_urls', '页面导航'), ('sys_imgs', '系统图标'), ('other', '其他')], default='page_urls', help_text='对应模块（CharField）', max_length=60, verbose_name='对应模块'),
        ),
    ]