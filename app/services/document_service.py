from sqlalchemy.orm import Session
from app.models import Document

def insert_document(db: Session, title, content, source, source_id, embedding):
    doc = Document(
        title=title,
        content=content,
        source=source,
        source_id=source_id,
        embedding=embedding
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def get_all_documents(db:Session):
   return db.query(Document).order_by(Document.id).all()


def search_similar(db: Session, query_embedding, limit=5):
    return (
        db.query(Document)
        .order_by(Document.embedding.cosine_distance(query_embedding))
        .limit(limit)
        .all()
    )
