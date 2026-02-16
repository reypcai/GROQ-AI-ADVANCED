# 🚀 Groq AI Advanced

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-black)

Production-ready local backend that integrates **Groq LLM API** with:

- ✅ Persistent conversation memory (SQLite)
- ✅ Basic RAG (Retrieval Augmented Generation)
- ✅ Rate limiting
- ✅ Internal API authentication
- ✅ Structured logging
- ✅ CLI interface
- ✅ Docker support
- ✅ Deployment-ready architecture

---

# 📌 Important

> This application runs locally, but model inference runs on Groq's infrastructure.

Models are **not downloaded locally**.  
All inference happens via:

```
https://api.groq.com/
```

---

# 🧠 What is Groq?

Groq provides ultra-fast LLM inference using specialized **LPU hardware**, optimized for:

- ⚡ Low latency
- 🚀 High throughput
- 💰 Cost efficiency
- 🧠 Large-scale model inference

Access models via API key:

👉 https://console.groq.com/

---

# 🔑 How to Create a Groq API Key

1. Go to: https://console.groq.com/
2. Sign up or log in
3. Navigate to **API Keys**
4. Click **Create API Key**
5. Copy your key
6. Add it to your `.env` file

⚠️ Never commit your API key to GitHub.

---

# ⚙️ Environment Configuration

Create a file named `.env`:

```env
GROQ_API_KEY=your_real_key_here
GROQ_MODEL=groq/compound-mini
INTERNAL_API_KEY=local_secure_key
```

---

## 🔍 Environment Variables Explained

| Variable | Description |
|-----------|------------|
| `GROQ_API_KEY` | Your secret Groq API key |
| `GROQ_MODEL` | Model name to use |
| `INTERNAL_API_KEY` | Authentication key for local API access |

---

# 🤖 Available Models

| Model | Requests/Day | Tokens/Min | Use Case | Cost Level |
|-------|--------------|------------|----------|------------|
| `groq/compound-mini` | 250 | 70k | Testing, CLI, lightweight apps | 🟢 Lowest |
| `groq/compound` | 250 | 70k | More structured responses | 🟡 Medium |
| `llama3-8b` | 14,400 | 6k | General purpose | 🟡 Medium |
| `llama-3.3-70b` | 1,000 | 12k | Advanced reasoning | 🔴 Higher |
| `llama-guard` | — | — | Moderation only | — |

---

## 🎯 Default Model Used

```
groq/compound-mini
```

Why?

- Lowest cost
- High token throughput
- Ideal for portfolio projects
- Good balance performance

---

# 🏗 Architecture Overview

```
Client (CLI / HTTP)
        │
        ▼
FastAPI Backend
        │
        ▼
Rate Limiter
        │
        ▼
Authentication
        │
        ▼
SQLite Memory
        │
        ▼
RAG (TF-IDF Retrieval)
        │
        ▼
Groq API
        │
        ▼
LLM Inference (Cloud)
        │
        ▼
Response
```

---

# 📂 Project Structure

```
groq-ai-advanced/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── groq_client.py
│   ├── routes.py
│   ├── memory.py
│   ├── rag.py
│   ├── rate_limiter.py
│   ├── auth.py
│   └── logger.py
│
├── data/
│   └── knowledge.txt
│
├── cli.py
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🧠 Core Features

---

## 1️⃣ Persistent Memory (SQLite)

- Stores user + AI messages
- Retrieves last conversation context
- Enables contextual dialogue

File:
```
memory.db
```

---

## 2️⃣ RAG (Retrieval Augmented Generation)

- Loads knowledge base from:
```
data/knowledge.txt
```
- Uses TF-IDF vectorization
- Retrieves most relevant context
- Injects into LLM prompt

Improves domain-specific accuracy.

---

## 3️⃣ Rate Limiting

- 200 requests per 24 hours
- Prevents API overuse
- Protects cost exposure

---

## 4️⃣ Internal API Authentication

All `/chat` requests must include header:

```
x-api-key: your_internal_key
```

Prevents unauthorized usage.

---

## 5️⃣ Logging

Structured logging via Python logging module.

Extendable with:

- JSON logs
- Monitoring systems
- Error tracking tools

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/groq-ai-advanced.git
cd groq-ai-advanced
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Mac/Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment

Copy:

```bash
cp .env.example .env
```

Edit `.env` and insert your real keys.

---

# ▶ Run Local API

```bash
uvicorn app.main:app --reload
```

Access Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run CLI Mode

```bash
python cli.py
```

---

# 🐳 Run with Docker

## Build image

```bash
docker build -t groq-ai .
```

## Run container

```bash
docker run -p 8000:8000 groq-ai
```

---

# 💰 Cost Control Strategy

To reduce cost:

- Limit `max_tokens`
- Keep prompts concise
- Use RAG for precision
- Avoid unnecessary retries
- Monitor daily usage

---

# 🔒 Security Best Practices

- Never expose `GROQ_API_KEY`
- Keep `.env` in `.gitignore`
- Rotate keys periodically
- Use backend-only API calls
- Protect deployed endpoint

---

# 🛠 Production Improvements (Future)

- Redis-based distributed rate limiting
- PostgreSQL instead of SQLite
- Real embeddings (not TF-IDF)
- Streaming responses (SSE)
- React frontend
- Multi-user authentication
- SaaS billing integration
- CI/CD pipeline
- Monitoring (Prometheus / Grafana)

---

# 📜 License

MIT License

---

# 👤 Author

Your Name  
Built with Groq + FastAPI  

---

# ⭐ If you like this project

Give it a star ⭐ on GitHub.