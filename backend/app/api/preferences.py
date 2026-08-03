from fastapi import APIRouter, Depends

from app.api.dependencies import get_preference_parser
from app.matching.models import ParsePreferenceRequest, StructuredPreferences
from app.matching.service import PreferenceParser

router = APIRouter(prefix="/preferences", tags=["preferences"])


@router.post("/parse", response_model=StructuredPreferences)
async def parse_preferences(
    request: ParsePreferenceRequest,
    parser: PreferenceParser = Depends(get_preference_parser),
) -> StructuredPreferences:
    return await parser.parse_preferences(request.description)
