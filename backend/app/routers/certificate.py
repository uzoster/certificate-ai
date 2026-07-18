from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.certificate import (
    CertificateCreate,
    CertificateUpdate
)
from app.services.certificate_service import *


router = APIRouter(
    prefix="/certificate",
    tags=["Certificate"]
)


@router.post("/")
def create(data: CertificateCreate,
           db: Session = Depends(get_db)):

    return create_certificate(db, data)


@router.get("/")
def certificates(db: Session = Depends(get_db)):
    return get_all(db)


@router.get("/{certificate_id}")
def one(certificate_id: int,
        db: Session = Depends(get_db)):

    certificate = get_one(db, certificate_id)

    if not certificate:
        raise HTTPException(404, "Certificate topilmadi")

    return certificate


@router.put("/{certificate_id}")
def update(
        certificate_id: int,
        data: CertificateUpdate,
        db: Session = Depends(get_db)
):

    certificate = update_certificate(
        db,
        certificate_id,
        data
    )

    if not certificate:
        raise HTTPException(
            status_code=404,
            detail="Certificate topilmadi"
        )

    return certificate

@router.delete("/{certificate_id}")
def remove(certificate_id: int,
           db: Session = Depends(get_db)):

    certificate = delete(db, certificate_id)

    if not certificate:
        raise HTTPException(404, "Certificate topilmadi")

    return {
        "message": "Deleted"
    }