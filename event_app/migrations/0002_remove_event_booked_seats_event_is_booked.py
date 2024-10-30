# Generated by Django 5.1.2 on 2024-10-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="booked_seats",
        ),
        migrations.AddField(
            model_name="event",
            name="is_booked",
            field=models.BooleanField(default=False),
        ),
    ]
