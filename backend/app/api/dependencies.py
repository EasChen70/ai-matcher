from app.llm.fake import FakeLLMClient
from app.matching.service import PreferenceParser


def get_preference_parser() -> PreferenceParser:
    return PreferenceParser(FakeLLMClient())
