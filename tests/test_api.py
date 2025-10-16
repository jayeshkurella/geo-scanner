import pytest
from django.test import Client

pytestmark = pytest.mark.django_db  

def test_admin_route():
    client = Client()
    response = client.get("/admin/")
    assert response.status_code in [200, 302]  # 302 if redirect to login
