# Generated by Django 3.2.6 on 2021-08-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('weekday', models.CharField(max_length=9)),
                ('band', models.CharField(max_length=32)),
                ('available', models.BooleanField()),
            ],
        ),
    ]