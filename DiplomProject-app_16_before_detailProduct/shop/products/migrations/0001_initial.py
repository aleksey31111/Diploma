# Generated by Django 4.1 on 2022-09-15 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Категория устройства')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории устройста')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания категории')),
            ],
            options={
                'verbose_name': 'Категория устройства',
                'verbose_name_plural': 'Категории устройств',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='device_image/%Y', verbose_name='Фото')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('short_description', models.CharField(blank=True, max_length=300, verbose_name='Краткое описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-time'],
            },
        ),
    ]
