def test_get_customers(client):
    response = client.get("/api/v1/user/")
    assert response.status_code == 200


def test_get_cleaner(client):
    response = client.get("/api/v1/cleaner/")
    assert response.status_code == 200
