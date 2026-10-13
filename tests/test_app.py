import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest FUNCTIONAL FITNESS" in response.data


def test_home_page_contains_all_programs(client):
    response = client.get("/")
    assert b"Fat Loss (FL)" in response.data
    assert b"Muscle Gain (MG)" in response.data
    assert b"Beginner (BG)" in response.data


def test_program_selection(client):
    response = client.get("/?program=Fat+Loss+(FL)")
    assert response.status_code == 200
    assert b"5x5 Back Squat" in response.data


def test_program_api_fat_loss(client):
    response = client.get("/?program=Fat+Loss+(FL)")
    assert b"2,000 kcal" in response.data


def test_program_api_muscle_gain(client):
    response = client.get("/?program=Muscle+Gain+(MG)")
    assert b"3,200 kcal" in response.data


def test_program_api_beginner(client):
    response = client.get("/?program=Beginner+(BG)")
    assert b"120g/day" in response.data


def test_list_programs(client):
    response = client.get("/api/programs")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "Fat Loss (FL)" in json_data["programs"]


def test_unknown_program(client):
    response = client.get("/?program=Unknown")
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness & Gym" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_gym_metrics(client):
    response = client.get("/api/metrics")
    assert response.status_code == 200
    assert response.get_json()["total_capacity"] == 50
