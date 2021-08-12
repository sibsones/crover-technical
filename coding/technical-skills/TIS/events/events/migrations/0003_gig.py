# Generated by Django 3.2.6 on 2021-08-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_booking_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('weekday', models.CharField(max_length=9)),
                ('band', models.CharField(max_length=32)),
            ],
        ),
    ]