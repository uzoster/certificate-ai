from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.app.core.database import Base


class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True)
    fullname = Column(String)
    course = Column(String)
    trainer = Column(String)
    background = Column(String)
    pdf = Column(String)
    qr = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)