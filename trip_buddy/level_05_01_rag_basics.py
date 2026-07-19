import os
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- OUR RAG TOOL (The Librarian) ---
def search_secret_documents() -> str:
    """Reads the private company database to find secret information."""
    print(f"\n--- Tool: Search Secret Documents --- The AI is opening the secret_knowledge.txt file! ---\n")
    
    # 1. We open the text file with the secret knowledge
    with open("secret_knowledge.txt", "r", encoding="utf-8") as file:
        secret_text = file.read()
        
    # 2. We hand all the text directly to the robot's brain!
    return secret_text


# --- THE RAG AGENT ---
root_agent = Agent(
    name="SecretAgent",
    model=my_model,
    # The instruction is incredibly strict to prevent hallucinations!
    instruction="""You are a VIP hotel concierge. You must ALWAYS use the search_secret_documents tool before answering questions. 
    ONLY answer using the facts you find in that document. If the answer is not in the document, you must say 'I am sorry, I do not have clearance for that.'""",
    tools=[search_secret_documents]
)