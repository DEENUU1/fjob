import pytest
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from offers.models import Offers
from report.models import ReportMessage

User = get_user_model()


@pytest.fixture
def create_user_offer():
    user = User.objects.create(username="testuser", password="testpassword")
    offer = Offers.objects.create(title="Test Offer")
    return user, offer


@pytest.mark.django_db
def test_report_message_str(create_user_offer):
    user, offer = create_user_offer
    message = "This is a test report message."
    report_message = ReportMessage.objects.create(
        message=message, offer=offer, user=user
    )
    expected_str = f"{offer} | {message[:50]}"
    assert report_message.__str__() == expected_str


@pytest.mark.django_db
def test_report_message_is_new(create_user_offer):
    user, offer = create_user_offer
    report_message = ReportMessage.objects.create(
        message="Test message", offer=offer, user=user
    )
    report_message.date_created = timezone.now() - timedelta(days=2)
    report_message.save()
    assert not report_message.is_new

    report_message.date_created = timezone.now() - timedelta(hours=23)
    report_message.save()
    assert report_message.is_new


@pytest.mark.django_db
def test_report_message_ordering(create_user_offer):
    user, offer = create_user_offer
    report_message1 = ReportMessage.objects.create(
        message="Message 1", offer=offer, user=user
    )
    report_message2 = ReportMessage.objects.create(
        message="Message 2", offer=offer, user=user
    )
    messages = ReportMessage.objects.all()
    assert messages[0] == report_message1
    assert messages[1] == report_message2


@pytest.mark.django_db
def test_report_message_reviewed(create_user_offer):
    user, offer = create_user_offer
    report_message = ReportMessage.objects.create(
        message="Test message", offer=offer, user=user
    )
    assert report_message.reviewed is False
    report_message.reviewed = True
    report_message.save()
    assert report_message.reviewed is True
