import os
import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.adk import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types

app = FastAPI(title="Trip Buddy AI API")

# This tells the API to accept traffic from our local HTML file
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In a real enterprise app, add your specific domain here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

my_model = os.getenv("MODEL_NAME")

web_agent = Agent(
    name="WebAgent",
    model=my_model,
    instruction="You are a helpful travel assistant. Keep your responses friendly, but short (under 3 sentences)."
)

engine = InMemoryRunner(agent=web_agent, app_name="TripAPI")
engine.auto_create_session = True

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_with_agent(request: ChatRequest):
    print(f"\n--- 🌐 RECEIVED WEB REQUEST: {request.message} ---\n")
    
    formatted_message = types.Content(
        role="user", 
        parts=[types.Part(text=request.message)]
    )
    
    fresh_session_id = str(uuid.uuid4())
    final_answer = ""
    
    for event in engine.run(
        user_id="web_user", 
        session_id=fresh_session_id, 
        new_message=formatted_message
    ):
        if event.content and event.content.parts and event.content.parts[0].text:
            final_answer += event.content.parts[0].text
            
    return {"ai_response": final_answer.strip()}