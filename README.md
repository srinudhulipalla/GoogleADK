# 🤖 Agentic AI Journey: From Beginner to Boss!

Welcome to AI learning repository! 

Imagine being able to build a team of tiny, invisible robots inside your computer. You can teach them to do math, search the live internet, and even talk to each other to solve puzzles for you. That is what **Agentic AI** is!

Here you can learn building these AI robots from scratch using the **Google Agent Development Kit (ADK)** in Python. I have saved every single step of chapter as a different "Level." 

---

## 🛠️ What You Need to Play (The Setup)

Even if you have never coded before, you can do this. Just follow these 3 steps:

### 1. Get a Coding Playground
Download a free code editor like **Cursor** or **Visual Studio Code (VS Code)**. This is where we write our robot instructions.

### 2. Install Python
Download **Python** from `python.org`. 
🚨 **Super Important:** When installing on Windows, make sure you check the box that says **"Add Python to PATH"** on the very first screen!

### 3. Install `uv` (Our Robot Organizer)
Open your terminal (Command Prompt or Mac Terminal) and paste the command for your computer to install `uv`:
*   **Windows:** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
*   **Mac/Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`

---

## 🚀 How to Start the Project

Open this project folder in your code editor, open a new terminal window, and type these commands one by one to build your robot workspace:

1. `uv venv` *(Creates a safe bubble for our code)*
2. `.venv\Scripts\activate` *(Turns the bubble on for Windows)* OR `source .venv/bin/activate` *(For Mac/Linux)*
3. `uv pip install google-adk` *(Downloads the Google AI robot parts)*

**The Secret Key:**
Create a file named exactly `.env` in the main folder and put your free Google Gemini API key inside it like this:

`GOOGLE_API_KEY=your_key_here`

`MODEL_NAME=gemini-3.1-flash-lite-preview` *(OR any other model you preferred)*

---

## 📂 The Library of Levels (Folder Structure)

All of the robot code is safely stored inside the `trip_buddy` folder. All of them are named by levels so you can go through the chapters in the same way:

| File Name | What You Will Learned Here! |
| :--- | :--- |
| `level_01_01_first_agent.py` | **The Brain:** Building a simple AI that can chat. |
| `level_01_02_agent_with_tools.py` | **The Hands:** Giving the AI tools to do real math and search the internet. |
| `level_01_03_multi_agent.py` | **The Team:** Making two robots pass messages like a relay race. |
| `level_02_01_short_term_memory.py` | **The Whiteboard:** Teaching robots to save and read temporary memory. |
| `level_02_02_long_term_memory.py` | **The Notebook:** Saving the AI's memory to a permanent hard drive file! |
| `level_03_01_manager_agent.py` | **The Manager:** Dynamic routing to automatically hand off tasks to the right specialist. |
| `level_04_01_human_in_loop.py` | **Safety First:** Forcing the AI to pause and ask for human approval before dangerous actions. |
| `level_05_01_rag_basics.py` | **Open Book Test:** Teaching the AI to read a secret text file before answering. |
| `level_05_02_smart_rag.py` | **The Librarian:** Keyword searching through massive text rulebooks. |
| `level_05_03_csv_rag.py` | **The Data Analyst:** Reading structured rows and prices from a CSV spreadsheet. |
| `level_05_04_folder_rag.py` | **The Detective:** Scanning an entire folder of files to combine clues into one answer. |
| `level_05_05_sql_rag.py` | **The Database Admin:** Connecting the AI directly to a real local SQL database! |

---

## 🎮 How to Run the Code (The Magic Switch)

Because you have so many levels, use the `__init__.py` file as a magic train track switch. 

**Step 1:** Open `trip_buddy/__init__.py`.

**Step 2:** Change the text to point to the level you want to play with. For example, if you want to run Level 1, make it say: 
`from .level_01_01_first_agent import root_agent`

**Step 3:** Open your terminal and run this exact command: 
`adk run trip_buddy`

Say hello to your new AI buddies! 🎉