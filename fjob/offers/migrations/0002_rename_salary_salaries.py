# Generated by Django 4.2.5 on 2023-09-22 20:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("offers", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Salary",
            new_name="Salaries",
        ),
    ]
