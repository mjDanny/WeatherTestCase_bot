import telebot
import requests

# токен бота
bot = telebot.TeleBot("7892936533:AAGuNkyBFE4FoRevtRbSZH0LV3Jkn_hFrsE")
api_key = "26dc97fc134c73687eae072439f6efed"
start_message = "Привет. Я бот для получения информации о погоде"


# стартовое сообщение
@bot.message_handler(commands=["start"])
def start(message):
    # Выводим приветствие
    bot.send_message(message.from_user.id, start_message)


@bot.message_handler(content_types=["text"])
def weather(message):
    # Получаем город из сообщения пользователя
    city = message.text
    # составляем запрос к api
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}"
    # Отправляем запрос
    weather_data = requests.get(url).json()
    # Получаем температуру в городе из сообщения пользователя
    temperature = weather_data["main"]["temp"]
    # составляем ответ
    weather = f"Сейчас в городе {city} {temperature} °C"
    # Составляем ответ
    bot.send_message(message.from_user.id, weather)


if __name__ == "__main__":
    bot.polling(non_stop=True, interval=0)
