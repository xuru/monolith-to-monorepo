import pytest
from rest_framework.test import APIClient
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_authenticated_client(api_client):
    def _create_authenticated_client(user):
        from django.conf import settings

        payload = JSONWebTokenAuthentication.jwt_create_payload(user)
        token = JSONWebTokenAuthentication.jwt_encode_payload(payload)
        api_client.credentials(HTTP_AUTHORIZATION=f"{settings.JWT_AUTH_HEADER_PREFIX} {token}")
        return api_client

    yield _create_authenticated_client

    # Clear the authorization header
    api_client.credentials()
