# Generated by Django 4.2.5 on 2023-10-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="read",
            field=models.BooleanField(default=False),
        ),
    ]