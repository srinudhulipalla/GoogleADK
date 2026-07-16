import os
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- THIS IS OUR AGENT ---
root_agent = Agent(
    name="RoadTripBuddy",
    model=my_model,
    instruction="You are a fun travel assistant for family road trips in Karnataka. Keep your answers short and fun!"    
)