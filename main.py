import requests

API_KEY = "bc39f5bd4441fa1eb194f7803f33f677"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        name = data["name"]
        country = data["sys"]["country"]
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        print(f"\n🌍 Location: {name}, {country}")
        print(f"🌤️ Weather: {weather}")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
    else:
        print("❌ City not found or API error!")

city = input("Enter the Name of Any City >>  ")
get_weather(city)
