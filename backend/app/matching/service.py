from app.llm.client import LLMClient
from app.matching.models import StructuredPreferences

SYSTEM_PROMPT = """
Convert the user's natural-language partner preferences into structured data matching the provided JSON schema.

Follow these rules:

Include only preferences explicitly stated or clearly implied by the user.
Do not invent, assume, or add missing preferences.
Separate ordinary preferences from explicit dealbreakers.
Treat something as a dealbreaker only when the user clearly describes it as unacceptable or required.
Do not infer sensitive characteristics, including race, ethnicity, religion, sexuality, health conditions, or political beliefs.
Normalize equivalent wording into concise, consistent terms.
Use empty lists or null values for information the user did not provide.
Return only valid JSON matching the provided schema, with no additional commentary.
"""

class PreferenceParser:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    async def parse_preferences(self, description: str) -> StructuredPreferences:
        # Use the LLM client to parse the preferences
        return await self.llm_client.generate_structured(
            system_prompt = SYSTEM_PROMPT,
            user_prompt = description,
            output_model = StructuredPreferences,
        )