# Generated by Django 4.1 on 2022-10-04 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_profitableproposition_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfitableProposition',
        ),
        migrations.DeleteModel(
            name='ProfitablePropositionCategory',
        ),
    ]
