# backend/responses.py
import random
import json
from django.http import HttpResponse

OPENWEATHER_API_KEY = "59c9f123b60d327aac00144fec861ab5"

def get_first_response(request, slug=None):
    # 1.1 Initial message
    message = "Hello! I am your chatbot. I can help you with anything unless you ask me to do something illegal."
    return HttpResponse(json.dumps({"message": message}))


last_message = None

def bot_response(request, message):
    global last_message  
    try:
        message_data = json.loads(message)
        text = message_data.get('text', '')
    except (json.JSONDecodeError, TypeError):
        text = message

    # 1.4 Check for repeated message
    if last_message == text:
        response = {
            "message": "STOP REPEATING YOURSELF"
        }
    # 1.2 Images
    elif "gimme image" in text.lower():
        random_number = random.randint(1, 1000)
        image_url = f"https://picsum.photos/200/300?id={random_number}"
        response = {
            "message": f'<img src="{image_url}" alt="Random Image">'
        }
    # 1.3 Wikipedia links
    elif "tell me about" in text.lower():
        topic = text.split("tell me about", 1)[1].strip()
        topic_url = topic.replace(" ", "_")
        response = {
            "message": f'<a href="https://en.wikipedia.org/wiki/{topic_url}" target="_blank">Click here for more information on {topic}</a>'
        }
    # 1.5 When the user types in weather in <city>, for example, weather in Pori, the bot should respond back with the weather in Pori. Use some external Web API to fetch the weather.
    elif "weather in" in text.lower():
        city = text.split("weather in", 1)[1].strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        try:
            data = request.get(url, timeout=5).json()
            if data.get("cod") == 200:
                main = data["main"]
                weather = data["weather"][0]
                weather_info = (
                    f"Weather in {city}:\n"
                    f"Temp: {main['temp']}°C\n"
                    f"Pressure: {main['pressure']} hPa\n"
                    f"Humidity: {main['humidity']}%\n"
                    f"Description: {weather['description']}"
                    )
            else:
                weather_info = "City Not Found"
        except Exception as e:
            weather_info = f"Error fetching weather data: {e}"
        response = {"message": weather_info}
    # 1.6 Help command
    elif "help" in text.lower():
        response = {
            "message": "I can help you with the following:\n"
                       "- Ask me to 'Gimme image' to get a random image.\n"
                       "- Ask me to 'Tell me about ...' to get a Wikipedia link.\n"
                       "- Ask me for the 'Weather in <city>' to get current weather information."
        }
    else:
        response = {
            "message": "I can only respond to 'Gimme image' or 'Tell me about ...'."
        }
    last_message = text

    return response