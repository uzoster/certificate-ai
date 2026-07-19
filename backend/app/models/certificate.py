from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.core.database import Base


class Certificate(Base):

    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(String, unique=True, nullable=False)

    fullname = Column(String, nullable=False)

    course = Column(String, nullable=False)

    trainer = Column(String, nullable=False)

    background = Column(String)

    # Certificate PNG
    image = Column(String)

    # Certificate PDF
    pdf = Column(String)

    # QR Code
    qr = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)