from gensim.models import Word2Vec
from app.ingestion.preprocess import clean_text
import os
from glob import glob

def load_docs(folder):
    texts = []
    for file in glob(f"{folder}/*"):
        with open(file, "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts

def train_model(directories):
    all_sentences = []
    for folder in directories:
        for text in load_docs(folder):
            tokens = clean_text(text)
            all_sentences.append(tokens)
    # train
    model = Word2Vec(
        sentences=all_sentences,
        vector_size=300,
        window=5,
        min_count=1,
        workers=4
    )
    model.save("word2vec.model")
    print("Word2Vec model trained and saved.")

if __name__ == "__main__":
    train_model(["data/faqs", "data/confluence"])
