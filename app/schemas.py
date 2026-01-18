from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FAQRequest(BaseModel):
    question: str
    answer: str
    source_name: Optional[str]
    embedding: List[float]

class FAQResponse(BaseModel):
    id: int
    question: str
    answer: str
    source_name: Optional[str]
    created_at: datetime
    similarity: float | None = None

    class Config:
        from_attributes = True  # Updated from orm_mode = True for Pydantic v2

class SearchTextRequest(BaseModel):
    query: str
    