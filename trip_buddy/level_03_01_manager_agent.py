import os
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- ROBOT 1: The Destination Picker ---
destination_agent = Agent(
    name="DestinationPicker",
    model=my_model,
    # The description is SUPER important. It tells the Manager WHEN to use this robot!
    description="Use this agent if the user wants to pick a travel destination or city to visit.",
    instruction="You help the user pick a destination in Karnataka. Keep it short and fun."
)

# --- ROBOT 2: The Packing Expert ---
packing_agent = Agent(
    name="PackingExpert",
    model=my_model,
    # The description tells the Manager to route packing questions here!
    description="Use this agent if the user is asking what to pack or needs a packing list.",
    instruction="You are a packing expert. Tell the user 3 specific items they need to pack."
)

# --- THE BOSS: The Manager Agent (Dynamic Router) ---
# Instead of a rigid Workflow, the Boss is an Agent that decides on the fly!
root_agent = Agent(
    name="ManagerAgent",
    model=my_model,
    instruction="You are the Trip Manager. Greet the user, figure out what they need, and transfer them to the right specialist.",
    
    # We hand the Manager with a list of its sub-agents right here!
    sub_agents=[destination_agent, packing_agent]
)