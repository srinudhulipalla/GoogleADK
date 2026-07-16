import os
from google.adk import Agent, Workflow
from google.genai import types

my_model = os.getenv("MODEL_NAME")

# --- ROBOT 1: The Destination Picker ---
destination_agent = Agent(
    name="DestinationPicker",
    model=my_model,
    instruction="Pick one random, beautiful travel destination in Karnataka. Return ONLY the name of the place and nothing else (like 'Hampi' or 'Coorg').",
    
    # temperature to 2.0 (maximum creativity) so it picks new places!
    generate_content_config=types.GenerateContentConfig(temperature=2.0)
)

# --- ROBOT 2: The Packing Expert ---
packing_agent = Agent(
    name="PackingExpert",
    model=my_model,
    instruction="You are a packing expert. The other robot will hand you a city name. Tell me exactly what 3 specific items I need to pack for a trip there, and make it sound fun!"
)

# --- THE BOSS: The Workflow ---
root_agent = Workflow(
    name="TeamTripBuddy",
    edges=[("START", destination_agent, packing_agent)]
)