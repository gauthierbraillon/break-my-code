"""
Feature 0: Hello World — the app must be reachable and identify itself.

ATDD RED phase: these tests must fail before implementation exists.
"""

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_homepage_returns_200():
    """The app is reachable at the root URL."""
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_contains_app_title():
    """The page identifies itself as Break My Code."""
    response = client.get("/")
    assert "Break My Code" in response.text


def test_homepage_is_html():
    """The root URL serves HTML."""
    response = client.get("/")
    assert "text/html" in response.headers["content-type"]
