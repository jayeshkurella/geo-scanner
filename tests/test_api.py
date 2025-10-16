from app import app

def test_admin_route():
    client = app.test_client()
    response = client.get("/admin/")
    assert response.status_code in [200]  # OK or redirect to login
