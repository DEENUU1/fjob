# Generated by Django 4.2.5 on 2023-10-25 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContractType",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Contract Type",
                "verbose_name_plural": "Contract Types",
                "ordering": ("-name",),
            },
        ),
        migrations.CreateModel(
            name="ExperienceLevel",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Experience Level",
                "verbose_name_plural": "Experience Levels",
                "ordering": ("-name",),
            },
        ),
        migrations.CreateModel(
            name="Localization",
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
                ("country", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("region", models.CharField(blank=True, max_length=255, null=True)),
                ("street", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Localization",
                "verbose_name_plural": "Localizations",
                "ordering": ("-country",),
            },
        ),
        migrations.CreateModel(
            name="Website",
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
                ("name", models.CharField(max_length=255)),
                ("url", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Website",
                "verbose_name_plural": "Websites",
                "ordering": ("-name",),
            },
        ),
        migrations.CreateModel(
            name="WorkSchedule",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Work Schedule",
                "verbose_name_plural": "Work Schedules",
                "ordering": ("-name",),
            },
        ),
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
                    "salary_schedule",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "Monthly"), (2, "Yearly"), (3, "Hourly")],
                        null=True,
                    ),
                ),
                (
                    "type",
                    models.IntegerField(
                        blank=True, choices=[(1, "Brutto"), (2, "Netto")], null=True
                    ),
                ),
                (
                    "contract_type",
                    models.ManyToManyField(blank=True, to="offers.contracttype"),
                ),
                (
                    "work_schedule",
                    models.ManyToManyField(blank=True, to="offers.workschedule"),
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
                ("url", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("skills", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "company_logo",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("is_remote", models.BooleanField(default=False)),
                ("is_hybrid", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_promoted", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(blank=True, null=True)),
                ("date_finished", models.DateTimeField(blank=True, null=True)),
                ("date_scraped", models.DateTimeField(auto_now=True)),
                (
                    "experience_level",
                    models.ManyToManyField(blank=True, to="offers.experiencelevel"),
                ),
                (
                    "localizations",
                    models.ManyToManyField(blank=True, to="offers.localization"),
                ),
                ("salary", models.ManyToManyField(blank=True, to="offers.salaries")),
                (
                    "website",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="offers.website",
                    ),
                ),
            ],
            options={
                "verbose_name": "Offer",
                "verbose_name_plural": "Offers",
                "ordering": ("-date_scraped",),
            },
        ),
    ]
