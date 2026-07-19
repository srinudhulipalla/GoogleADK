import os
import sqlite3 
from google.adk import Agent

my_model = os.getenv("MODEL_NAME")

# --- SETUP: Building the Database ---
# This runs invisibly to make sure we have a database to search!
def setup_database():
    conn = sqlite3.connect("company_data.db") # Creates a file called company_data.db
    cursor = conn.cursor()
    
    # We create a table with columns, just like a real database
    cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, role TEXT, department TEXT)")
    
    # We add 3 pretend employees if the table is empty
    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO employees (name, role, department) VALUES ('Alice', 'Engineer', 'IT')")
        cursor.execute("INSERT INTO employees (name, role, department) VALUES ('Bob', 'Manager', 'Sales')")
        cursor.execute("INSERT INTO employees (name, role, department) VALUES ('Charlie', 'Support', 'IT')")
        conn.commit()
    conn.close()

setup_database() # We turn the database on!


# --- OUR DATABASE RAG TOOL ---
def search_employee_database(department_name: str) -> str:
    """Searches the massive SQL database to find employees in a specific department."""
    print(f"\n--- Tool: Search Employee Database --- Running a SQL query for the '{department_name}' department! ---\n")
    
    # 1. We connect to the database
    conn = sqlite3.connect("company_data.db")
    cursor = conn.cursor()
    
    # 2. We ask the database for the exact data the AI wants
    cursor.execute("SELECT name, role FROM employees WHERE department = ?", (department_name,))
    results = cursor.fetchall()
    conn.close()
    
    # 3. We turn the database rows into a friendly message for the AI
    if results:
        found_people = []
        for row in results:
            found_people.append(f"{row[0]} works as a {row[1]}")
        return "\n".join(found_people)
    else:
        return f"No employees found in the {department_name} department."


# --- THE DATABASE AGENT ---
root_agent = Agent(
    name="HR_Database_Bot",
    model=my_model,
    instruction="""You are a helpful HR assistant. 
    When someone asks who works in a department, use the search_employee_database tool. 
    Pass ONLY the exact department name (like 'IT' or 'Sales') to the tool.""",
    tools=[search_employee_database]
)