import pytest
from django.contrib.auth.models import Permission, Group
from django.contrib.auth import get_user_model


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
