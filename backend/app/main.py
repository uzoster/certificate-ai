from fastapi import FastAPI

from backend.app.core.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Certificate AI")


@app.get("/")
def home():
    return {"message": "Certificate AI API ishlayapti 🚀"}