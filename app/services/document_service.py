from sqlalchemy.orm import Session
from app.models import FAQ
from sqlalchemy import func

def insert_faq(db: Session, question, answer, source_name, embedding):
    new_faq = FAQ(
        question=question,
        answer=answer,
        source_name=source_name,
        embedding=embedding
    )
    db.add(new_faq)
    db.commit()
    db.refresh(new_faq)
    return new_faq

def search_similar(db: Session, query_embedding, threshold=0.6, limit=1):
    # Distance: 0 = identical, 2 = opposite
    distance_func = FAQ.embedding.cosine_distance(query_embedding)
    
    # Similarity: 1 = identical, -1 = opposite
    similarity_score = func.coalesce((1 - distance_func), 0.0 ).label("similarity")

    return (
        db.query(FAQ, similarity_score)
        .filter(similarity_score >= threshold) # The 0.8 Threshold
        .order_by(distance_func)
        .all()
    )

def get_all_faqs(db: Session):
    return db.query(FAQ).all()