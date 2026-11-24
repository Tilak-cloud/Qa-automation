import pytest
import requests
from requests.exceptions import Timeout
def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code==200
    
    data=response.json()

    assert data["id"]==1
    assert data["userId"]==1

def test_create_post():
    url="https://jsonplaceholder.typicode.com/posts"

    payload={
        "title": "My first API test",
        "body": "Learning API automation",
        "userId": 1,
    }

    response=requests.post(url, json=payload)

    assert response.status_code == 201

    data=response.json()

    assert data["title"] == "My first API test"
    assert data["body"] == "Learning API automation"
    assert data["userId"] == 1

def test_get_invalid_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")

    assert response.status_code==404

def test_get_post_response_validation():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "title" in data
    assert "body" in data

    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert data["id"] == 1

def test_get_posts_by_user():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": 1}
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for post in data:
        assert post["userId"] == 1

@pytest.mark.parametrize("post_id",[1,2,3])
def test_get_post_with_multiple_params(post_id):

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=5
        # params={
        #     "userId": 1,
        #     "id": 1
        # }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"]==post_id
    #assert len(data) == 1
    # assert data[0]["userId"] == 1
    # assert data[0]["id"] == 1

def test_get_post_with_headers():

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=headers
    )

    assert response.status_code == 200

    assert response.headers["Content-Type"].startswith(
        "application/json"
    )

    data = response.json()

    assert data["id"] == 1

def test_get_post_with_auth_header():

    headers = {
        "Authorization": "Bearer demo_token_123"
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

def test_get_post_with_timeout():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1