from datetime import timedelta

import pytest
from django.utils import timezone
from offers.models import salaries, offers
from django.contrib.auth.models import Permission, Group
from django.contrib.auth import get_user_model
from payment.models import Package, UserPackage
from contact.models import Contact


UserModel = get_user_model()


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


@pytest.mark.django_db
def test_custom_user_creation():
    group = Group.objects.create(name="Test Group")
    permission = Permission.objects.create(
        codename="test_permission", name="Test Permission", content_type_id=1
    )

    User = get_user_model()
    user = User.objects.create_user(
        email="test@example.com",
        password="testpassword",
        username="XXXXXXXX",
    )

    user.groups.add(group)
    user.user_permissions.add(permission)

    assert user.email == "test@example.com"
    assert user.check_password("testpassword")
    assert user.groups.first() == group
    assert user.user_permissions.first() == permission

    assert str(user) == "XXXXXXXX"


@pytest.mark.django_db
def test_package_creation():
    package = Package.objects.create(
        name="Test Package",
        price=1000,
        has_signals=True,
        num_of_signals=50,
        is_free=False,
    )

    assert package.name == "Test Package"
    assert package.price == 1000
    assert package.has_signals == True
    assert package.num_of_signals == 50
    assert package.is_free == False

    assert package.cents_to_dollar == 10.0

    assert str(package) == "Test Package - 1000$"


@pytest.mark.django_db
def test_user_package_creation():
    user = UserModel.objects.create_user(
        email="test@example.com",
        password="testpassword",
        username="XXXXXXXX",
    )

    package = Package.objects.create(
        name="Test Package",
        price=1000,
        has_signals=True,
        num_of_signals=50,
        is_free=False,
    )

    user_package = UserPackage.objects.create(
        user=user,
        package=package,
        active=True,
        stripe_checkout_id="stripe_checkout_id",
        custom_id="custom_id",
        free_uses=5,
    )

    assert user_package.user == user
    assert user_package.package == package
    assert user_package.active == True
    assert user_package.stripe_checkout_id == "stripe_checkout_id"
    assert user_package.custom_id == "custom_id"
    assert user_package.free_uses == 5

    assert str(user_package) == f"{user} - {package}"


@pytest.mark.django_db
def test_contact_creation():
    contact = Contact.objects.create(
        name="Test user",
        email="test@example.com",
        content="Test body message",
    )

    assert contact.name == "Test user"
    assert contact.email == "test@example.com"
    assert contact.content == "Test body message"
    assert contact.read == False

    assert str(contact) == f"{contact.name} - {contact.email}"
