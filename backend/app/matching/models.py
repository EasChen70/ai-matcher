#define profile, preferences, and compatibility-result schemas
from pydantic import BaseModel, Field 

#verifies before sending to llm
class ParsePreferenceRequest(BaseModel):
    description: str = Field(min_length=10, max_length = 200, example = "I want a partner who is kind, intelligent, and has a good sense of humor.")


class StructuredPreferences(BaseModel):
    # data of user preferences after parsing by llm
    desired_traits: list[str] = Field(default_factory=list)
    preferred_interests: list[str] = Field(default_factory=list)
    lifestyle_preferences: list[str] = Field(default_factory=list)
    dealbreakers: list[str] = Field(default_factory=list)
    relationship_goal: str | None = None

