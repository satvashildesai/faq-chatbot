from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.schemas import FAQRequest, FAQResponse, SearchTextRequest
from app.services.document_service import insert_faq, search_similar, get_all_faqs
from app.ingestion.preprocess import clean_text
from app.ingestion.embed_utils import get_embedding
from app.schemas import SearchTextRequest

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/faqs", response_model=FAQResponse)
def add_document(doc: FAQRequest, db: Session = Depends(get_db)):
    return insert_faq(
        db,
        question=doc.q_clean,
        answer=doc.a_clean,
        source_name=doc.source_name,
        embedding=doc.embedding
    )

@app.get("/faqs", response_model=list[FAQResponse])
def get_documents(db: Session = Depends(get_db)):
    return get_all_faqs(db)

@app.post("/search/text", response_model=list[FAQResponse])
def search_by_text(body: SearchTextRequest, db: Session = Depends(get_db)):
    tokens = clean_text(body.query)
    query_embedding = get_embedding(tokens)
    results = search_similar(db, query_embedding)
    
    formatted_results = []
    for faq, score in results:
        faq.similarity = round(float(score), 4)
        formatted_results.append(faq)
    
    return formatted_results