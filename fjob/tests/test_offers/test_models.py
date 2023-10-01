from datetime import timedelta

import pytest
from django.utils import timezone
from offers.models import salaries, offers


@pytest.fixture
def sample_salary_data():
    return {
        "salary_from": 50000,
        "salary_to": 70000,
        "currency": "USD",
        "contract_type": "Full-Time",
        "work_schedule": "Monday to Friday",
    }


@pytest.fixture
def sample_offer_data(sample_salary_data):
    return {
        "title": "Software Engineer",
        "offer_id": "12345",
        "url": "https://example.com/job/12345",
        "street": "123 Main St",
        "region": "Tech Town",
        "description": "A job description.",
        "remote": True,
        "hybrid": False,
        "country": "USA",
        "city": "Techville",
        "date_created": timezone.now(),
        "date_finished": timezone.now() + timedelta(days=30),
        "experience_level": "Entry-Level",
        "skills": "Python, Django, SQL",
        "company_name": "Tech Co",
        "company_logo": "https://example.com/logo.png",
    }


@pytest.mark.django_db
def test_create_and_retrieve_salary():
    salary_data = {
        "salary_from": 50000,
        "salary_to": 70000,
        "currency": "USD",
        "contract_type": "Full-Time",
        "work_schedule": "Monday to Friday",
    }
    salary = salaries.Salaries.objects.create(**salary_data)

    assert salaries.Salaries.objects.count() == 1
    retrieved_salary = salaries.Salaries.objects.first()
    assert retrieved_salary.salary_from == 50000
    assert retrieved_salary.salary_to == 70000


@pytest.mark.django_db
def test_create_and_retrieve_offer(sample_offer_data, sample_salary_data):
    salary = salaries.Salaries.objects.create(**sample_salary_data)
    offer = offers.Offers.objects.create(**sample_offer_data)

    offer.salary.set([salary])

    assert offers.Offers.objects.count() == 1
    retrieved_offer = offers.Offers.objects.first()
    assert retrieved_offer.title == "Software Engineer"
    assert retrieved_offer.salary.first().salary_from == 50000
    assert retrieved_offer.salary.first().salary_to == 70000
    assert retrieved_offer.is_new is True
