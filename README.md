# 🤖 AURA – AI Voice Assistant

AURA is an AI-powered **voice and chat assistant** built using **Python**, **FastAPI**, and **LLaMA 3 (via Ollama)**.  
It allows users to interact with a locally hosted AI model through a **web frontend** or **REST API**, demonstrating real-world usage of LLMs and agentic AI workflows.

---

## 🚀 Features

- AI-powered conversational assistant
- Local inference with LLaMA 3 via Ollama
- FastAPI backend with REST API endpoints
- Swagger UI for API testing
- Simple HTML/JavaScript frontend
- Modular, beginner-friendly architecture

---

## 🧠 How It Works

1. User types a query in the frontend or Swagger UI  
2. FastAPI backend receives the request  
3. Request is forwarded to LLaMA 3 model via Ollama  
4. Model generates a response  
5. Response is returned to the frontend in real time  

---

## 🛠 Tech Stack

| Category | Technology |
|----------|-----------|
| Backend  | Python, FastAPI |
| LLM      | Ollama (LLaMA 3) |
| Frontend | HTML, JavaScript |
| API Testing | Swagger UI |
| Server   | Uvicorn |

---

## 📁 Project Structure

> ❗ `venv/` and `__pycache__/` are excluded from the repository

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9+
- Ollama installed: https://ollama.com

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/your-username/AURA-Voice-Assistant.git
cd AURA-Voice-Assistant
# 2. Install dependencies
pip install -r requirements.txt

# 3. Pull the LLaMA 3 model
ollama pull llama3

# 4. Start Ollama (keep this running in background)
ollama run llama3

# 5. Start the FastAPI backend server
uvicorn api:app --reload

# 6. Open Swagger UI for API testing
# Open in browser: http://127.0.0.1:8000/docs

# 7. Open the frontend
# Option 1: Open index.html directly in browser
# Option 2: Use Python HTTP server
python -m http.server 5500
# Then open in browser: http://localhost:5500
