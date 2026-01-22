import requests

def get_weather(city):
    api_key = "a3f2fb5de6e4a856cea6375190b134d2"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def main():
    city = input("Введите город: ")
    data = get_weather(city)

    if data is None:
        print("❌ Город не найден или ошибка API")
        return

    city_name = data['name']
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    print(
        f"Погода в {city_name}:\n"
        f"🌡 Температура: {temp}°C\n"
        f"💧 Влажность: {humidity}%\n"
        f"🌬 Ветер: {wind} м/с\n"
        f"{weather.capitalize()}"
    )


main()
