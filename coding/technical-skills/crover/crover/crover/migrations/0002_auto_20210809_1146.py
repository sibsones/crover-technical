# Generated by Django 3.2.6 on 2021-08-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crover', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='temperature',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='graph',
            name='x',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='graph',
            name='y',
            field=models.BinaryField(),
        ),
    ]
