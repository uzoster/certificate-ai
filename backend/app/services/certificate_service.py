import uuid

from sqlalchemy.orm import Session

from app.models.certificate import Certificate

from app.services.qr_service import generate_qr


def create_certificate(db: Session, data):

    uid = str(uuid.uuid4())

    qr = generate_qr(uid)

    certificate = Certificate(

        uuid=uid,

        fullname=data.fullname,

        course=data.course,

        trainer=data.trainer,

        background=data.background,

        pdf="",

        qr=qr

    )

    db.add(certificate)

    db.commit()

    db.refresh(certificate)

    return certificate




def get_all(db: Session):
    return db.query(Certificate).all()


def get_one(db: Session, certificate_id: int):
    return db.query(Certificate).filter(
        Certificate.id == certificate_id
    ).first()


def get_uuid(db: Session, uid: str):
    return db.query(Certificate).filter(
        Certificate.uuid == uid
    ).first()


def delete(db: Session, certificate_id: int):

    certificate = get_one(db, certificate_id)

    if certificate:
        db.delete(certificate)
        db.commit()

    return certificate


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