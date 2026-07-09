from google.adk import Agent, Workflow

# --- ROBOT 1: The Destination Picker ---
destination_agent = Agent(
    name="DestinationPicker",
    model="gemini-3.1-flash-lite-preview",
    instruction="Pick one random, beautiful travel destination in Karnataka. Return ONLY the name of the place and nothing else (like 'Hampi' or 'Coorg')."
)

# --- ROBOT 2: The Packing Expert ---
packing_agent = Agent(
    name="PackingExpert",
    model="gemini-3.1-flash-lite-preview",
    instruction="You are a packing expert. The other robot will hand you a city name. Tell me exactly what 3 specific items I need to pack for a trip there, and make it sound fun!"
)

# --- THE BOSS: The Workflow ---
# This connects our robots like a relay race!
# It says: START the race -> go to DestinationPicker -> pass the baton to PackingExpert
root_agent = Workflow(
    name="TeamTripBuddy",
    edges=[("START", destination_agent, packing_agent)]
)