# Generated by Django 5.0.4 on 2024-04-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]
