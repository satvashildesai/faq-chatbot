from sqlalchemy import Column, Integer, Text, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base
from pgvector.sqlalchemy import Vector

class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False) # The FAQ question
    answer = Column(Text, nullable=False)   # The FAQ answer
    embedding = Column(Vector(300))         # Embedding of the QUESTION ONLY
    source_name = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
    