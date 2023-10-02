import pytest
from django.contrib.auth import get_user_model
from payment.models import Package, UserPackage


UserModel = get_user_model()


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
