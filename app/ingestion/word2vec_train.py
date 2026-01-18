import re
from gensim.models import Word2Vec
from app.ingestion.preprocess import clean_text
from glob import glob

def load_and_parse_faq_data(folder):
    """Parses files to extract all text for training."""
    sentences = []
    for file in glob(f"{folder}/*"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            # Split by 'Q:' or 'A:' to treat each as a separate sentence/context
            parts = re.split(r'[QA]:', content)
            for part in parts:
                if part.strip():
                    tokens = clean_text(part.strip())
                    if tokens:
                        sentences.append(tokens)
    return sentences

def train_model(directories):
    all_sentences = []
    for folder in directories:
        sentences = load_and_parse_faq_data(folder)
        all_sentences.extend(sentences)
    
    # Train the model on the full vocabulary
    model = Word2Vec(
        sentences=all_sentences,
        vector_size=300, # This matches to Vector(300) DB column
        window=5,
        min_count=1,
        workers=4
    )
    model.save("word2vec.model")
    print(f"Word2Vec model trained on {len(all_sentences)} text segments.")

if __name__ == "__main__":
    train_model(["data/faqs"])