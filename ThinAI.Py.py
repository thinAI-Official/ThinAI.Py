import random
import requests

# Predefined responses
predefined_responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you?": "I'm a bot, so I don't have feelings, but I'm here to help you!",
    "what is your name?": "I'm Th1n.AI, your virtual assistant.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is AI?": "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines.",
    "what is machine learning?": "Machine learning is a subset of AI that enables computers to learn and improve from experience without being explicitly programmed.",
    "what is the capital of France?": "The capital of France is Paris.",
    "who is the president of the United States?": "As of my last update, the President of the United States is Joe Biden.",
    "what is the largest mammal?": "The blue whale is the largest mammal on Earth.",
    "what is the boiling point of water?": "The boiling point of water at standard atmospheric pressure is 100 degrees Celsius (212 degrees Fahrenheit).",
    "what is the speed of light?": "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
    "how do airplanes fly?": "Airplanes fly by generating lift through their wings, which is created by the shape of the wings and the forward motion of the aircraft.",
    "who wrote 'Romeo and Juliet'?": "William Shakespeare wrote 'Romeo and Juliet'.",
    "what is the formula for the area of a circle?": "The formula for the area of a circle is A = πr^2, where A is the area and r is the radius of the circle.",
    "what is the square root of 144?": "The square root of 144 is 12.",
    "what is the atomic number of carbon?": "The atomic number of carbon is 6.",
    "what is the chemical formula for water?": "The chemical formula for water is H2O.",
    "what is the longest river in the world?": "The longest river in the world is the Nile River in Africa.",
    "what is the tallest mountain in the world?": "The tallest mountain in the world is Mount Everest in the Himalayas.",
    "what is the capital of Japan?": "The capital of Japan is Tokyo.",
    "what is the population of China?": "As of my last update, the population of China is approximately 1.4 billion people.",
    "what is the meaning of life?": "I'm not sure anyone knows the true meaning of life, but it's a question philosophers and thinkers have pondered for centuries."
}

# OpenWeather API key
WEATHER_API_KEY = '5eb83a7d0bfbf5c44112df0096089d77'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {city} is currently {weather_description} with a temperature of {temperature}°C."
    else:
        return "I couldn't fetch the weather information."

def get_bot_response(user_message):
    user_message = user_message.lower()
    for keyword, response in predefined_responses.items():
        if keyword in user_message:
            return response
    if "weather" in user_message:
        city = input("Which city's weather do you want to know? ")
        return get_weather(city)
    return "I'm still learning. Can you tell me more?"

print("Th1n.AI: Hello! I'm Th1n.AI. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Th1n.AI: Goodbye! Have a great day.")
        break
    response = get_bot_response(user_input)
    print("Th1n.AI:", response)
