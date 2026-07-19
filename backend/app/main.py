from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.database import Base, engine

from app.models.certificate import Certificate
# from app.routers.ai import router as ai_router

from app.routers.certificate import router as certificate_router
from app.routers.verify import router as verify_router

# Database yaratish
Base.metadata.create_all(bind=engine)


# FastAPI App
app = FastAPI(
    title="AI Certificate Studio",
    version="1.0.0"
)


# Static Files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


# Routers
app.include_router(certificate_router)
app.include_router(verify_router)
# app.include_router(ai_router)

# Home
@app.get("/")
def home():
    return {
        "status": "ok",
        "project": "AI Certificate Studio",
        "version": "1.0.0"
    }