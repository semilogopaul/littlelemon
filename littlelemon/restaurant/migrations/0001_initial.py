# Generated by Django 5.0.7 on 2024-07-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.IntegerField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField(max_length=6)),
                ('BookingDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('ID', models.IntegerField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField(max_length=5)),
            ],
        ),
    ]
