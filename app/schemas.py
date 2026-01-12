from pydantic import BaseModel
from typing import List, Optional

class DocumentCreate(BaseModel):
    title: Optional[str]
    content: str
    source: Optional[str]
    source_id: Optional[str]
    embedding: List[float]


class DocumentResponse(BaseModel):
    id: int
    title: Optional[str]
    content: str
    source: Optional[str]
    source_id: Optional[str]

    class Config:
        orm_mode = True

class SearchRequest(BaseModel):
    embedding: List[float]

class SearchTextRequest(BaseModel):
    query: str
