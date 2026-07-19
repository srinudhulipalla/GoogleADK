import os
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- OUR DETECTIVE RAG TOOL ---
def search_all_documents(keyword: str) -> str:
    """Searches every text file inside the knowledge_base folder for a keyword."""
    folder_path = "knowledge_base"
    print(f"\n--- Tool: Search All Documents --- Opening the filing cabinet to search all documents for '{keyword}'! ---\n")
    
    # We create an empty list to hold the clues we find
    found_clues = []
    
    # 1. Check if the folder actually exists
    if not os.path.exists(folder_path):
        return "Error: The knowledge_base folder is missing!"
        
    # 2. Loop through every single file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Only read text files
            file_path = os.path.join(folder_path, filename)
            
            # 3. Open the file and look for the keyword
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                if keyword.lower() in content.lower():
                    # If we find a clue, we save the file's name and its text!
                    found_clues.append(f"Found in {filename}:\n{content}")
                    
    # 4. If we found clues, glue them together and send them to the AI
    if found_clues:
        return "\n\n".join(found_clues)
    else:
        return f"I searched all documents, but found nothing about '{keyword}'."


# --- THE RESEARCHER AGENT ---
root_agent = Agent(
    name="LeadResearcher",
    model=my_model,
    instruction="""You are a lead travel researcher. 
    When asked a question, identify the most important single keyword. 
    Use the search_all_documents tool to search the filing cabinet. 
    Combine the information you find into a friendly answer.""",
    tools=[search_all_documents]
)