# ----------------- IMPORTS -----------------
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import traceback

# ----------------- FASTAPI APP -----------------
app = FastAPI(
    title="Aura AI Voice Assistant",
    description="FastAPI backend using Ollama (Agentic AI)",
    version="1.0"
)

# ----------------- CORS (allow frontend access) -----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- MODELS -----------------
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    reply: str

# ----------------- CONVERSATION MEMORY -----------------
conversation_memory = []

# ----------------- FUNCTION TO CALL OLLAMA -----------------
def ask_ollama(prompt: str) -> str:
    """
    Sends the user prompt to Ollama LLM and returns the response.
    Keeps a short conversation memory of last 10 interactions.
    """
    conversation_memory.append(f"User: {prompt}")
    full_prompt = "\n".join(conversation_memory) + "\nAura:"

    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",  # Ollama local API
            json={
                "model": "llama3",
                "prompt": full_prompt,
                "stream": False
            },
            timeout=60  # 60 sec timeout
        )
        # Debug: print raw response in backend terminal
        print("Ollama raw response:", response.text)

        answer = response.json().get("response", "AI service returned no response")
    except Exception as e:
        print("Ollama Exception:", traceback.format_exc())
        answer = f"AI service is not available ({str(e)})"

    conversation_memory.append(f"Aura: {answer}")

    # Keep last 10 interactions only
    if len(conversation_memory) > 20:
        conversation_memory.pop(0)

    return answer

# ----------------- API ENDPOINT: ASK -----------------
@app.post("/ask", response_model=AnswerResponse)
def ask_ai_endpoint(data: QuestionRequest):
    """
    POST /ask
    Request: {"question": "your question"}
    Response: {"reply": "AI answer"}
    """
    reply_text = ask_ollama(data.question)
    return {"reply": reply_text}

# ----------------- API ENDPOINT: RESET -----------------
@app.post("/reset")
def reset_chat():
    """
    POST /reset
    Clears the conversation memory
    """
    conversation_memory.clear()
    return {"status": "Conversation memory cleared"}