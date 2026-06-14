import requests
import os
import time
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

load_dotenv()

API_KEY = os.getenv("API_KEY")

emoji_map = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Snow": "❄️",
    "Thunderstorm": "⛈️",
    "Drizzle": "🌦️",
    "Mist": "🌫️",
    "Fog": "🌫️",
    "Haze": "🌫️"
}

while True:
    city = input("\nEnter city (q to quit): ")

    if city.lower() == "q":
        break

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        condition = data["weather"][0]["main"]
        emoji = emoji_map.get(condition, "🌍")

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        offset = data["timezone"]
        utc_now = datetime.now(timezone.utc)
        local_time = utc_now + timedelta(seconds=offset)
        current_time = local_time.strftime("%I:%M %p")

        print("=" * 40)
        print(f"📍 Weather in {city.capitalize()}")
        print("=" * 40)
        print(f"Time : {current_time}")
        print(f"{emoji} {description.capitalize()}")
        print(f"🌡️ Temperature : {temp}°C")
        print(f"🥵 Feels Like  : {feels_like}°C")
        print(f"💧 Humidity    : {humidity}%")
        print(f"🌬️ Wind Speed  : {wind} m/s")
        print(f"📈 Pressure    : {pressure} hPa")
        print("=" * 40)

    else:
        print("City not found or API error.")