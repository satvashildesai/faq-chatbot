from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.schemas import DocumentCreate, DocumentResponse, SearchRequest
from app.services.document_service import insert_document, search_similar, get_all_documents
from app.ingestion.preprocess import clean_text
from app.ingestion.embed_utils import get_embedding
from app.schemas import SearchTextRequest

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/documents", response_model=DocumentResponse)
def add_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    return insert_document(
        db,
        title=doc.title,
        content=doc.content,
        source=doc.source,
        source_id=doc.source_id,
        embedding=doc.embedding
    )

@app.get("/documents", response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    return get_all_documents(db)


@app.post("/search", response_model=list[DocumentResponse])
def search_docs(body: SearchRequest, db: Session = Depends(get_db)):
    results = search_similar(db, body.embedding)
    return results

@app.post("/search/text", response_model=list[DocumentResponse])
def search_by_text(body: SearchTextRequest, db: Session = Depends(get_db)):
    tokens = clean_text(body.query)
    query_embedding = get_embedding(tokens)
    results = search_similar(db, query_embedding)
    return results
