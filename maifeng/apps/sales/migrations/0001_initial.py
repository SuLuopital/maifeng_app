# Generated by Django 3.0 on 2022-02-20 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wares', '0002_auto_20220220_1402'),
        ('users', '0004_auto_20220220_1402'),
        ('store', '0003_auto_20220220_1436'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='交易单号（CharField）', max_length=60, verbose_name='交易单号')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='交易时间（DateTimeField）', null=True, verbose_name='交易时间')),
                ('last_edited_date', models.DateTimeField(auto_now=True, help_text='最后编辑时间（DateTimeField）', null=True, verbose_name='最后编辑时间')),
                ('deleted', models.CharField(choices=[('0', '未删除'), ('1', '已删除')], default='0', help_text='是否删除（CharField，可选值：0，1）', max_length=1, verbose_name='是否删除')),
                ('created_by', models.ForeignKey(blank=True, help_text='创建人ID（ForeignKey）', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sales_cb', to='users.UserExtension', verbose_name='创建人ID')),
                ('group', models.ManyToManyField(blank=True, help_text='可见分组', related_name='Sales_group', to='auth.Group', verbose_name='可见分组')),
                ('last_edited_by', models.ForeignKey(blank=True, help_text='最后编辑人ID（ForeignKey）', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sales_eb', to='users.UserExtension', verbose_name='最后编辑人ID')),
            ],
            options={
                'verbose_name': '交易订单',
                'verbose_name_plural': '交易订单',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='SalesDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, default=0, help_text='交易数量（CharField）', null=True, verbose_name='交易数量')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='交易时间（DateTimeField）', null=True, verbose_name='交易时间')),
                ('last_edited_date', models.DateTimeField(auto_now=True, help_text='最后编辑时间（DateTimeField）', null=True, verbose_name='最后编辑时间')),
                ('deleted', models.CharField(choices=[('0', '未删除'), ('1', '已删除')], default='0', help_text='是否删除（CharField，可选值：0，1）', max_length=1, verbose_name='是否删除')),
                ('created_by', models.ForeignKey(blank=True, help_text='创建人ID（ForeignKey）', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SalesDetails_cb', to='users.UserExtension', verbose_name='创建人ID')),
                ('group', models.ManyToManyField(blank=True, help_text='可见分组', related_name='SalesDetails_group', to='auth.Group', verbose_name='可见分组')),
                ('last_edited_by', models.ForeignKey(blank=True, help_text='最后编辑人ID（ForeignKey）', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SalesDetails_eb', to='users.UserExtension', verbose_name='最后编辑人ID')),
                ('name', models.ForeignKey(blank=True, help_text='交易单号（ForeignKey）', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sales', to='sales.Sales', verbose_name='交易单号')),
                ('shop', models.ForeignKey(blank=True, help_text='门店（ForeignKey）', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SalesDetails_shop', to='store.Shop', verbose_name='门店')),
                ('waresku', models.ForeignKey(blank=True, help_text='商品SKU（ForeignKey）', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SalesDetails_waresku', to='wares.WareSKU', verbose_name='商品SKU')),
            ],
            options={
                'verbose_name': '交易详情',
                'verbose_name_plural': '交易详情',
                'ordering': ['-name__name', 'waresku__code'],
            },
        ),
    ]