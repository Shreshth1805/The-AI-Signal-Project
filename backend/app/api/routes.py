from fastapi import APIRouter
from app.pipeline.orchestrator import run_pipeline

router = APIRouter()

@router.get("/")
async def health():
    return {"status": "running"}

@router.post("/generate")
async def generate(payload: dict):
    prompt = payload.get("prompt")
    return await run_pipeline(prompt)