import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

STOPWORDS = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> list[str]:
    # lowercase
    text = text.lower()
    # remove non-alphanumerics
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    # tokenize
    tokens = word_tokenize(text)
    # remove stopwords and short words
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    # lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens
