# Generated by Django 2.2 on 2019-04-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_auto_20190416_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(),
        ),
    ]
