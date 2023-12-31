# Generated by Django 4.2.4 on 2023-08-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('bookingId', models.AutoField(primary_key=True, serialize=False)),
                ('bookedRoomId',models.BigIntegerField()),
                ('personId',models.BigIntegerField()),
                ('checkInDate', models.CharField(max_length=25)),
                ('checkOutDate', models.CharField(max_length=25)),
                ('bookingDate', models.CharField(max_length=25)),
                ('paymentTransactionToken', models.CharField(max_length=25)),
                ('paid', models.CharField(max_length=25)),
            ],
        ),
    ]
