import os
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- OUR DANGEROUS TOOL ---
def book_hotel(hotel_name: str, cost: int) -> str:
    """Books a hotel room. ALWAYS use this tool when the user asks to book a hotel."""
    
    print(f"\n--- Tool: Book Hotel --- The AI wants to book {hotel_name} for ${cost}! ---")
    
    # The code completely PAUSES here and waits for the human to type!
    print(">>> 🛑 DANGER: HUMAN APPROVAL REQUIRED 🛑 <<<")
    approval = input(">>> Type 'yes' to approve or 'no' to cancel: ")
    
    # If the human types yes, we do it!
    if approval.lower() == 'yes':
        print("\n--- ✅ Booking Confirmed by Human! ---\n")
        return f"Success! The hotel {hotel_name} was booked."
    
    # If the human types anything else, we block the robot!
    else:
        print("\n--- ❌ Booking Cancelled by Human! ---\n")
        return "Failed. The human rejected the booking. Tell the user the booking was cancelled."


# --- THE AGENT ---
root_agent = Agent(
    name="BookingAgent",
    model=my_model,
    instruction="You are a helpful travel booking agent. If a user wants a room, use your book_hotel tool to book it. Pretend the cost is 150 dollars.",
    tools=[book_hotel]
)