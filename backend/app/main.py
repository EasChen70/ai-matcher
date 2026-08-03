from fastapi import FastAPI

from app.api.preferences import router as preferences_router

app = FastAPI(title = "AI Matcher API")

app.include_router(preferences_router)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}