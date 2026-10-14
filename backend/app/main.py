from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="Personal API App",
    version="0.1.0",
    description="Backend API for a personal AI Assistant",
)

@app.get("/health")
def health():
    return{"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        reply=f"You said: {request.message}"
    )