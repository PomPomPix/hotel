# Generated by Django 2.1.7 on 2019-04-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=30)),
                ('Special_request', models.CharField(max_length=280)),
            ],
        ),
    ]
