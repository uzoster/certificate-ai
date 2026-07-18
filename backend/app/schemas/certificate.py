from pydantic import BaseModel
from datetime import datetime


class CertificateCreate(BaseModel):
    fullname: str
    course: str
    trainer: str
    background: str = ""

class CertificateUpdate(BaseModel):
    fullname: str
    course: str
    trainer: str
    background: str = ""

class CertificateResponse(BaseModel):
    id: int
    uuid: str
    fullname: str
    course: str
    trainer: str
    background: str
    pdf: str | None = None
    qr: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True