# Generated by Django 4.1.7 on 2023-03-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('checkindate', models.DateField()),
                ('checkoutdate', models.DateField()),
            ],
        ),
    ]
