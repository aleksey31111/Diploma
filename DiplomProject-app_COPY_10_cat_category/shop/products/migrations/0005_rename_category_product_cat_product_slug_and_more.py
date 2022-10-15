# Generated by Django 4.1 on 2022-10-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_profitableproposition_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='cat',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
