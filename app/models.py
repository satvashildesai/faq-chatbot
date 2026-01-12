from sqlalchemy import Column, Integer, Text, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base
from pgvector.sqlalchemy import Vector

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    content = Column(Text, nullable=False)
    source = Column(String)
    source_id = Column(String)
    embedding = Column(Vector(300))
    created_at = Column(TIMESTAMP, server_default=func.now())
