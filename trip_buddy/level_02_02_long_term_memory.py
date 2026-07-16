import os
import json # 
from google.adk import Agent, Workflow
from google.genai import types

my_model = os.getenv("MODEL_NAME")

# --- THE PERMANENT NOTEBOOK (Long-Term Memory) ---
MEMORY_FILE = "robot_memory.json"

def get_memory_notebook() -> dict:
    """Opens the notebook file and reads it. If it doesn't exist, it makes a blank one."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {} # Return an empty dictionary if the file is missing

def save_to_notebook(data: dict):
    """Saves the updated memory back into the permanent file."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)

# --- TOOLS ---
def write_to_memory(key: str, value: str) -> str:
    """Writes important information to permanent memory."""
    notebook = get_memory_notebook() # 1. Open the book
    notebook[key] = value            # 2. Write the new info
    save_to_notebook(notebook)       # 3. Save the book
    
    print(f"\n--- Tool: Saved '{value}' to permanent hard drive! ---\n")
    return f"Successfully saved {key}."

def read_from_memory(key: str) -> str:
    """Reads information from permanent memory."""
    notebook = get_memory_notebook() # 1. Open the book
    value = notebook.get(key, "Nothing found.") # 2. Look for the key
    
    print(f"\n--- Tool: Remembered '{value}' from hard drive! ---\n")
    return value


# --- ROBOT 1: The Writer ---
destination_agent = Agent(
    name="DestinationPicker",
    model=my_model,
    instruction="Pick one random destination in Karnataka. Use the write_to_memory tool to save the city name with the key 'city'.",
    tools=[write_to_memory], 
    generate_content_config=types.GenerateContentConfig(temperature=2.0)
)

# --- ROBOT 2: The Reader ---
packing_agent = Agent(
    name="PackingExpert",
    model=my_model,
    instruction="You are a packing expert. Use the read_from_memory tool to find out what 'city' the user is going to. Then tell me 3 items to pack.",
    tools=[read_from_memory] 
)

# --- THE BOSS: The Workflow ---
root_agent = Workflow(
    name="TeamTripBuddy",
    edges=[("START", destination_agent, packing_agent)]
)