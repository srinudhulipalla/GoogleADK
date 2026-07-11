import os
from google.adk import Agent, Workflow
from google.genai import types

my_model = os.getenv("MODEL_NAME", "gemini-3.1-flash-lite-preview")

# --- THE SHARED BRAIN (State / Memory) ---
whiteboard = {}

def write_to_whiteboard(key: str, value: str) -> str:
    """Writes important information to the shared whiteboard."""
    whiteboard[key] = value
    print(f"\n--- Tool: Writing '{value}' to whiteboard under '{key}'!  ---\n")
    return f"Successfully saved {key}."

def read_from_whiteboard(key: str) -> str:
    """Reads information from the shared whiteboard."""
    value = whiteboard.get(key, "Nothing found.")
    print(f"\n--- Tool: Reading '{value}' from whiteboard! ---\n")
    return value


# --- ROBOT 1: The Writer ---
destination_agent = Agent(
    name="DestinationPicker",
    model=my_model,
    # We explicitly command the agent to use its tool to save the data!
    instruction="Pick one random destination in Karnataka. Use the write_to_whiteboard tool to save the city name with the key 'city'.",
    tools=[write_to_whiteboard], 
    generate_content_config=types.GenerateContentConfig(temperature=2.0)
)

# --- ROBOT 2: The Reader ---
packing_agent = Agent(
    name="PackingExpert",
    model=my_model,
    # We command this agent to look up the data before answering!
    instruction="You are a packing expert. Use the read_from_whiteboard tool to find out what 'city' the user is going to. Then tell me 3 items to pack.",
    tools=[read_from_whiteboard] 
)

# --- THE BOSS: The Workflow ---
root_agent = Workflow(
    name="TeamTripBuddy",
    edges=[("START", destination_agent, packing_agent)]
)