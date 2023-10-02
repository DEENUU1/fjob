# Generated by Django 4.2.5 on 2023-10-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Salaries",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("salary_from", models.IntegerField(blank=True, null=True)),
                ("salary_to", models.IntegerField(blank=True, null=True)),
                ("currency", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "contract_type",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "work_schedule",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
            options={
                "verbose_name": "Salary",
                "verbose_name_plural": "Salaries",
                "ordering": ("-salary_from",),
            },
        ),
        migrations.CreateModel(
            name="Offers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("offer_id", models.CharField(blank=True, max_length=255, null=True)),
                ("url", models.CharField(blank=True, max_length=255, null=True)),
                ("street", models.CharField(blank=True, max_length=255, null=True)),
                ("region", models.CharField(blank=True, max_length=255, null=True)),
                ("additional_data", models.JSONField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("remote", models.BooleanField(blank=True, null=True)),
                ("hybrid", models.BooleanField(blank=True, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("date_created", models.DateTimeField(blank=True, null=True)),
                ("date_finished", models.DateTimeField(blank=True, null=True)),
                (
                    "experience_level",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("skills", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "company_logo",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("date_scraped", models.DateTimeField(auto_now=True, null=True)),
                ("salary", models.ManyToManyField(to="offers.salaries")),
            ],
            options={
                "verbose_name": "Offer",
                "verbose_name_plural": "Offers",
                "ordering": ("-date_scraped",),
            },
        ),
    ]
