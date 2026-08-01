import asyncio
import pytest
from pydantic import ValidationError
from app.llm.fake import FakeLLMClient
from app.matching.models import StructuredPreferences, ParsePreferenceRequest
from app.matching.service import PreferenceParser

def test_preference_request_accepts_valid_description() -> None:
    request = ParsePreferenceRequest(
        description="I want someone kind and ambitious."
    )

    assert request.description == "I want someone kind and ambitious."


def test_preference_request_rejects_short_description() -> None:
    with pytest.raises(ValidationError):
        ParsePreferenceRequest(description="kind")


def test_parse_preferences_returns_structured_preferences() -> None:
    parser = PreferenceParser(FakeLLMClient())

    result = asyncio.run(
        parser.parse_preferences(
            "I want someone ambitious, funny, tall, active, and interested "
            "in travel. Smoking is a dealbreaker."
        )
    )

    assert isinstance(result, StructuredPreferences)

    assert result.desired_traits == [
        "ambitious",
        "funny",
        "tall",
    ]
    assert result.preferred_interests == [
        "fitness",
        "travel",
    ]
    assert result.lifestyle_preferences == ["active"]
    assert result.dealbreakers == ["smoking"]
    assert result.relationship_goal == "long-term relationship"