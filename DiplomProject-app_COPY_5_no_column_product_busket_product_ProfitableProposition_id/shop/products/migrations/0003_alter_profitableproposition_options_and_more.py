# Generated by Django 4.1 on 2022-09-27 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_profitablepropositioncategory_profitableproposition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profitableproposition',
            options={'ordering': ['-time'], 'verbose_name': 'Товар Выгодных Предложений', 'verbose_name_plural': 'Товары Выгодных Предложений'},
        ),
        migrations.AlterModelOptions(
            name='profitablepropositioncategory',
            options={'ordering': ['-time'], 'verbose_name': 'Категория устройства Выгодных Предложений', 'verbose_name_plural': 'Категории устройств Выгодных Предложений'},
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('create_database', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Товар в корзину',
                'verbose_name_plural': 'Корзина',
            },
        ),
    ]