# Generated by Django 4.2.4 on 2023-08-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomId', models.AutoField(primary_key=True, serialize=False)),
                ('roomtype', models.CharField(max_length=25)),
                ('roomNo', models.CharField(max_length=25)),
                ('aminities', models.CharField(max_length=25)),
                ('price', models.BigIntegerField()),
                ('isAvailable',models.IntegerField())
            ],
        ),
    ]
