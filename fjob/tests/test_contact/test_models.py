import pytest
from contact.models import Contact


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
