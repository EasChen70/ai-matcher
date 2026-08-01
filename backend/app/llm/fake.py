from typing import TypeVar

from pydantic import BaseModel

OutputT = TypeVar("OutputT", bound=BaseModel)

# A mock implementation of the LLMClient protocol for local testing and development.
class FakeLLMClient:
    async def generate_structured(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        output_model: type[OutputT],
    ) -> OutputT:
        # Simulate output generation from an LLM.
        return output_model.model_validate(
            {
                "desired_traits": ["ambitious", "funny", "tall"],
                "preferred_interests": ["fitness", "travel"],
                "lifestyle_preferences": ["active"],
                "dealbreakers": ["smoking"],
                "relationship_goal": "long-term relationship",
            }
        )