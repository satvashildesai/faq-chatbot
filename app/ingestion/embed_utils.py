import numpy as np
from gensim.models import Word2Vec

model = Word2Vec.load("word2vec.model")

def get_embedding(text_tokens: list[str]) -> list[float]:
    vectors = []
    for token in text_tokens:
        if token in model.wv:
            vectors.append(model.wv[token])
    if len(vectors) == 0:
        # if no tokens found, return zeros
        return np.zeros(model.vector_size).tolist()
    # average
    return np.mean(vectors, axis=0).tolist()
