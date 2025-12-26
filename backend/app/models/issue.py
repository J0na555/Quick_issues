from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.db.base import Base 


class Issue(Base):
    __tablename__ = "issues"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    
    user_id = Column(
        String,
        ForeignKey("users.id"),
        nullable=False, 
        index=True
    )

    title = Column(
        String,
        nullable=False,
        index=True
    )

    description = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = relationship("User", back_populates="issues")