# Generated by Django 5.1.2 on 2024-10-27 08:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking_app", "0002_booking_seats_reserved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="seats_reserved",
        ),
    ]