# Generated by Django 5.0.6 on 2024-06-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name=11)),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.IntegerField(max_length=6)),
                ('bookingdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField(max_length=5)),
            ],
        ),
    ]