import uuid

from sqlalchemy.orm import Session

from app.models.certificate import Certificate

from app.services.qr_service import generate_qr
from app.services.certificate_generator import generate_certificate
from app.services.pdf_service import generate_pdf


def create_certificate(db: Session, data):

    # UUID
    uid = str(uuid.uuid4())

    # QR Code
    qr_path = generate_qr(uid)

    # Certificate PNG
    certificate_image = generate_certificate(
        uuid=uid,
        fullname=data.fullname,
        course=data.course,
        trainer=data.trainer,
        background=data.background,
        qr_path=qr_path
    )

    # PDF
    pdf_path = generate_pdf(
        image_path=certificate_image,
        uuid=uid
    )

    # Database
    certificate = Certificate(
        uuid=uid,
        fullname=data.fullname,
        course=data.course,
        trainer=data.trainer,
        background=data.background,
        image=certificate_image,
        pdf=pdf_path,
        qr=qr_path
    )

    db.add(certificate)
    db.commit()
    db.refresh(certificate)

    return certificate


def get_all(db: Session):
    return db.query(Certificate).all()


def get_one(db: Session, certificate_id: int):
    return (
        db.query(Certificate)
        .filter(Certificate.id == certificate_id)
        .first()
    )


def get_uuid(db: Session, uid: str):
    return (
        db.query(Certificate)
        .filter(Certificate.uuid == uid)
        .first()
    )


def update_certificate(db: Session, certificate_id: int, data):

    certificate = get_one(db, certificate_id)

    if not certificate:
        return None

    certificate.fullname = data.fullname
    certificate.course = data.course
    certificate.trainer = data.trainer
    certificate.background = data.background

    db.commit()
    db.refresh(certificate)

    return certificate


def delete(db: Session, certificate_id: int):

    certificate = get_one(db, certificate_id)

    if not certificate:
        return None

    db.delete(certificate)
    db.commit()

    return certificate