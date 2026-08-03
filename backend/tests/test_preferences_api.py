from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_parse_preferences_endpoint_returns_structured_preferences() -> None:
    response = client.post(
        "/preferences/parse",
        json={
            "description": (
                "I want someone ambitious, funny, tall, active, and interested "
                "in travel. Smoking is a dealbreaker."
            )
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert body["desired_traits"] == ["ambitious", "funny", "tall"]
    assert body["preferred_interests"] == ["fitness", "travel"]
    assert body["lifestyle_preferences"] == ["active"]
    assert body["dealbreakers"] == ["smoking"]
    assert body["relationship_goal"] == "long-term relationship"


def test_parse_preferences_endpoint_rejects_short_description() -> None:
    response = client.post("/preferences/parse", json={"description": "kind"})

    assert response.status_code == 422
