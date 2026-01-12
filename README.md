# FAQ & Documentation Chatbot

This project is a learning-focused chatbot system built entirely using open-source tools. It ingests FAQs and documentation (such as Confluence exports), converts them into vector embeddings, stores them in PostgreSQL using pgvector, and performs semantic search to answer user questions.

The project is intentionally built in phases — starting with Word2Vec to understand embedding fundamentals, and later upgrading to modern transformer-based sentence embeddings like MiniLM or Sentence Transformers.

---

## 🚀 Features

- Built completely from scratch (no paid APIs, no OpenAI, no external LLMs)
- Word2Vec-based embeddings (Phase 1)
- Sentence Transformers / MiniLM (Phase 2 – planned)
- PostgreSQL + pgvector for vector storage
- FastAPI backend
- Semantic search over FAQs and documentation
- Modular and production-style architecture
- Easy upgrade path between embedding models

---

## 🧠 How It Works

```
User Query
   ↓
Text Preprocessing
   ↓
Embedding Model (Word2Vec / Sentence Transformer)
   ↓
pgvector (PostgreSQL)
   ↓
Cosine Similarity Search
   ↓
Top Matching Documents
   ↓
Response
```

---

## 🛠 Tech Stack

| Component        | Technology                          |
|-----------------|-------------------------------------|
| Language        | Python                              |
| Backend         | FastAPI                             |
| Database        | PostgreSQL 16                       |
| Vector Search   | pgvector                            |
| Embeddings      | Word2Vec (gensim), MiniLM (planned) |
| NLP Processing  | NLTK                                |
| ORM             | SQLAlchemy                          |
| Frontend        | React (planned)                     |

---

## 📁 Project Structure

```
faq_chatbot/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── deps.py
│   ├── services/
│   │   └── document_service.py
│   └── ingestion/
│       ├── preprocess.py
│       ├── embed_utils.py
│       ├── word2vec_train.py
│       └── ingest_documents.py
│
├── data/
│   ├── faqs/
│   └── confluence/
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/faq-chatbot.git
cd faq-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/faq_bot
```

---

### 5️⃣ Enable pgvector Extension

In PostgreSQL:

```sql
CREATE EXTENSION vector;
```

---

## 📥 Training Word2Vec (Phase 1)

Place your files inside:

```
data/faqs/
data/confluence/
```

Then run:

```bash
python -m app.ingestion.word2vec_train
```

---

## 📦 Ingest Documents

```bash
python -m app.ingestion.ingest_documents
```

---

## ▶️ Run the Server

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```
