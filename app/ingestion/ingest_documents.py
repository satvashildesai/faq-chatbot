from app.ingestion.preprocess import clean_text
from app.ingestion.embed_utils import get_embedding
from app.db import SessionLocal
from app.services.document_service import insert_document
import os
from glob import glob

def ingest_folder(folder, source):
    db = SessionLocal()
    for filepath in glob(f"{folder}/*"):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        tokens = clean_text(text)
        embedding = get_embedding(tokens)

        # Use filename as source_id
        source_id = os.path.basename(filepath)

        insert_document(
            db,
            title=source + "_" + source_id,
            content=text,
            source=source,
            source_id=source_id,
            embedding=embedding
        )
    db.close()

if __name__ == "__main__":
    ingest_folder("data/faqs", "faq")
    ingest_folder("data/confluence", "confluence")
    print("Ingestion done!")
