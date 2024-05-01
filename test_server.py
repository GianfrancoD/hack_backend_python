import pytest
import json
from app import app
import requests



def test_hack_1():
    client = app.test_client()
    with client:
        response = client.get('/users')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert "payload" in data
        assert data["payload"] == "success"



def test_hack_2():
    client = app.test_client()
    with client:
        response = client.post('/user')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert "payload" in data
        assert data["payload"] == "success"



def test_hack_3():
    client = app.test_client()
    with client:
        response = client.delete('/user')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert "payload" in data
        assert data["payload"] == "success"



def test_hack_4():
    client = app.test_client()
    with client:
        response = client.put('/user')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert "payload" in data
        assert "error" in data
        assert data["payload"] == "success"
        assert data["error"] == False



def test_hack_5():
    client = app.test_client()
    with client:
        response = client.get('/api/v1/users')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert "payload" in data
        assert data["payload"] == []




def test_hack_6():
    endpoint = 'http://localhost:5000/api/v1/user?email=foo@foo.foo&name=fooziman'
    response = requests.post(endpoint)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['payload'] == {
                                        'email': 'foo@foo.foo',
                                        'name': 'fooziman',
                                    }


def test_hack_7():
    with app.test_client() as client:
        data = {
            'email': 'foo@foo.foo',
            'name': 'fooziman',
            'id': '123'
        }
        endpoint = 'http://localhost:5000/api/v1/user/add'
        response = client.post(endpoint, data=data)
        assert response.status_code == 200
        assert response.get_json() == {
                                    'payload': {
                                        'email': 'foo@foo.foo',
                                        'name': 'fooziman',
                                        'id': '123'}
                                    }


def test_hack_8():
    with app.test_client() as client:
        data = {
            'email': 'foo@foo.foo',
            'name': 'fooziman',
            'id': '123'
        }
        endpoint = 'http://localhost:5000/api/v1/user/create'
        response = client.post(endpoint, json=data)
        assert response.status_code == 200
        assert response.get_json() == {
                                    'payload': {
                                        'email': 'foo@foo.foo',
                                        'name': 'fooziman',
                                        'id': '123'}
                                    }




if __name__ == '__main__':
    app.run()