# Generated by Django 4.2.5 on 2023-11-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scrapers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pagecontent",
            name="content_json",
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
