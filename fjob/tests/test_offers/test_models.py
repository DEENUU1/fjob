import pytest
from offers.models import (
    Website,
    ExperienceLevel,
    ContractType,
    WorkSchedule,
    Salaries,
    Localization,
    Offers,
)
from datetime import timedelta
from django.utils import timezone


@pytest.mark.django_db
def test_website_model():
    website = Website.objects.create(name="Example Website", url="https://example.com")
    assert website.__str__() == "Example Website"


@pytest.mark.django_db
def test_experience_level_model():
    experience_level = ExperienceLevel.objects.create(name="Senior")
    assert experience_level.__str__() == "Senior"


@pytest.mark.django_db
def test_contract_type_model():
    contract_type = ContractType.objects.create(name="Full-time")
    assert contract_type.__str__() == "Full-time"


@pytest.mark.django_db
def test_work_schedule_model():
    work_schedule = WorkSchedule.objects.create(name="9 to 5")
    assert work_schedule.__str__() == "9 to 5"


@pytest.mark.django_db
def test_salaries_model():
    salary = Salaries.objects.create(
        salary_from=50000, salary_to=60000, currency="USD", salary_schedule=1, type=1
    )
    assert salary.__str__() == "50000 - 60000"


@pytest.mark.django_db
def test_localization_model():
    localization = Localization.objects.create(
        country="USA", city="New York", region="NY", street="123 Main St"
    )
    assert localization.__str__() == "USA, New York, NY, 123 Main St"


@pytest.mark.django_db
def test_offers_model():
    website = Website.objects.create(name="Example Website", url="https://example.com")
    experience_level = ExperienceLevel.objects.create(name="Senior")

    offer = Offers.objects.create(
        title="Senior Developer Job",
        website=website,
    )

    offer.experience_level.set([experience_level])
    offer.salary.set(
        [
            Salaries.objects.create(
                salary_from=50000,
                salary_to=60000,
                currency="USD",
                salary_schedule=1,
                type=1,
            )
        ]
    )

    assert offer.__str__() == "Senior Developer Job"
    assert offer.is_new

    offer.date_scraped = timezone.now() - timedelta(days=2)
    offer.save()
    assert offer.is_new
