from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.certificate_service import get_uuid

router = APIRouter(
    prefix="/verify",
    tags=["Verify"]
)


@router.get("/{uuid}")
def verify(uuid: str,
           db: Session = Depends(get_db)):

    certificate = get_uuid(db, uuid)

    if not certificate:
        raise HTTPException(404, "Certificate topilmadi")

    return certificate