import re
import os
from glob import glob
from app.ingestion.preprocess import clean_text
from app.ingestion.embed_utils import get_embedding
from app.db import SessionLocal
from app.services.document_service import insert_faq 

def ingest_faq_folder(folder):
    """
    Parses Q&A files and stores them in the 'faqs' table 
    with 300-dimension embeddings of the questions.
    """
    db = SessionLocal()
    
    # Path to search for files
    search_path = os.path.join(folder, "*")
    
    for filepath in glob(search_path):
        if os.path.isdir(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find all Q: and A: pairs
        # Matches 'Q:' followed by question text, then 'A:' followed by answer text
        pairs = re.findall(r'Q:(.*?)\s*A:(.*?)(?=Q:|$)', content, re.DOTALL)

        if not pairs:
            print(f"Skipping {filepath}: No Q&A pairs found.")
            continue

        for question_text, answer_text in pairs:
            q_clean = question_text.strip()
            a_clean = answer_text.strip()

            # 1. Create embedding ONLY from the Question tokens
            # This is the '300 dimension' representation of the intent
            tokens = clean_text(q_clean)
            embedding = get_embedding(tokens)

            # 2. Use filename or a custom string as source_name
            source_name = os.path.basename(filepath)

            # 3. Insert into the new FAQ table
            insert_faq(
                db,
                question=q_clean,
                answer=a_clean,
                source_name=source_name,
                embedding=embedding
            )
            
    db.close()

if __name__ == "__main__":
    faq_dir = "data/faqs"
    if os.path.exists(faq_dir):
        ingest_faq_folder(faq_dir)
        print("Success: FAQ table populated with question-based embeddings.")
    else:
        print(f"Error: Directory {faq_dir} not found.")