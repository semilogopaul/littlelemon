# Generated by Django 5.0.7 on 2024-07-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(max_length=5, unique=True),
        ),
    ]
