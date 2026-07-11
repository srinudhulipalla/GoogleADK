from google.adk import Agent
import urllib.request

# --- THIS IS OUR First TOOL --- 
def calculate_driving_time(distance_km: int) -> str:
    """Calculates how many hours a road trip will take based on the distance in kilometers."""
    
    print(f"Tool: Calculating driving time for {distance_km} kilometers")

    # We pretend the car goes 50 kilometers per hour on average
    hours = distance_km / 50
    return f"The drive will take exactly {hours} hours."

# --- OUR SECOND TOOL: The Live Internet! ---
def get_live_weather(city: str) -> str:
    """Gets the real-time live weather from the internet for a specific city."""
    print(f"Tool: Checking the live internet for {city} weather")
    
    # 1. We prepare the web address. (We use a free weather site called wttr.in)
    safe_city = city.replace(" ", "+")
    url = f"https://wttr.in/{safe_city}?format=3"
    
    # 2. We pretend to be a normal web browser so the website lets us in
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    # 3. We read the page and send it back to the AI!
    response = urllib.request.urlopen(req)
    weather_text = response.read().decode('utf-8')
    
    return weather_text

# --- OUR THIRD TOOL: File Saver! ---
def save_itinerary_to_file(itinerary_text: str) -> str:
    """Saves the final road trip itinerary to a text file on the computer."""
    print(f"Tool: Saving the itinerary to a text file")
    
    # This automatically creates a file and writes the AI's text into it
    with open("road_trip_plan.txt", "w", encoding="utf-8") as file:
        file.write(itinerary_text)
        
    return "Success! The itinerary was saved to road_trip_plan.txt"

# --- THIS IS OUR AGENT ---
root_agent = Agent(
    name="RoadTripBuddy",
    model="gemini-3.1-flash-lite-preview",
    instruction="You are a fun travel assistant for family road trips in Karnataka. Keep your answers short and fun!",
    
    # We hand the tool to the robot right here!
    tools=[calculate_driving_time, get_live_weather, save_itinerary_to_file] 
)