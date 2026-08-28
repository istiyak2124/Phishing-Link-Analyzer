from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.app.models.database import Base


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)

    url = Column(String, nullable=False)

    domain = Column(String, nullable=False)

    risk_score = Column(Integer, nullable=False)

    verdict = Column(String, nullable=False)

    malicious = Column(Integer, nullable=False)

    suspicious = Column(Integer, nullable=False)

    harmless = Column(Integer, nullable=False)

    undetected = Column(Integer, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )