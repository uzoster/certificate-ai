from pydantic import BaseModel


class CertificateCreate(BaseModel):

    fullname: str

    course: str

    trainer: str

    background: str