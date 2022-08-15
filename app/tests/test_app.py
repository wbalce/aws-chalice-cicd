from chalice.test import Client
from app import app

def test_foo_function():
    with Client(app) as client:
        response = client.http.get('/')
        assert response.json_body == {'hello': 'world'}

