import os
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- OUR SMART RAG TOOL ---
def search_company_policies(keyword: str) -> str:
    """Searches the massive company policy book for a specific keyword and returns only the matching rules."""
    print(f"\n--- Tool: Search Company Policies --- Scanning the massive rulebook for the word: '{keyword}'! ---\n")
    
    try:
        with open("company_policies.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        # We look through every single line in the book...
        matching_lines = []
        for line in lines:
            # If the keyword is in the line, we save it!
            if keyword.lower() in line.lower():
                matching_lines.append(line.strip())
        
        # If we found matches, we send ONLY those lines back to the robot
        if matching_lines:
            return "\n".join(matching_lines)
        else:
            return f"No policies found for the keyword '{keyword}'."
            
    except FileNotFoundError:
        return "Error: The policy book is missing!"


# --- THE SMART RAG AGENT ---
root_agent = Agent(
    name="HR_Bot",
    model=my_model,
    # We teach the AI how to use the search engine by guessing a 1-word keyword!
    instruction="""You are a helpful HR assistant. 
    When an employee asks a question, figure out the most important word in their sentence. 
    Pass that single word into the search_company_policies tool to find the rule. 
    ONLY answer based on what the tool finds.""",
    tools=[search_company_policies]
)