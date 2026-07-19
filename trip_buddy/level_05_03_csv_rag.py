import os
import csv 
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- OUR SPREADSHEET RAG TOOL ---
def check_inventory(product_name: str) -> str:
    """Searches the store's CSV spreadsheet to find the price and stock of a product."""
    print(f"\n--- Tool: Check Inventory --- Scanning the spreadsheet for '{product_name}'! ---\n")
    
    try:
        # 1. We open the spreadsheet
        with open("inventory.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            # 2. We check every single row one by one
            for row in reader:
                # If we find a match, we send the row data to the AI!
                if product_name.lower() in row['Product'].lower():
                    return f"Found it! The {row['Product']} costs ${row['Price']} and we have {row['Stock']} in stock."
                    
        # 3. If the loop finishes and finds nothing:
        return f"Sorry, I could not find '{product_name}' in the spreadsheet."
        
    except FileNotFoundError:
        return "Error: The inventory.csv file is missing!"


# --- THE SPREADSHEET AGENT ---
root_agent = Agent(
    name="StoreClerk",
    model=my_model,
    instruction="""You are a helpful camping store clerk. 
    When a customer asks about a product, use the check_inventory tool to find it. 
    Tell them the price and how many are in stock. If it is out of stock (0), suggest they check back later!""",
    tools=[check_inventory]
)