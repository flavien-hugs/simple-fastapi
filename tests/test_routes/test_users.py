import json

def test_get_customers(client):
    response = client.get("/customer/")
    assert response.status_code == 200


def test_get_cleaner(client):
    response = client.get("/cleaner/")
    assert response.status_code == 200
