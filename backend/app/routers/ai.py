from fastapi import APIRouter

from app.services.ai_service import generate_background

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/background")
def create(prompt: str):

    image = generate_background(prompt)

    return {
        "image": image
    }