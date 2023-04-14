import logging
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types

weather_token = "6e8d79779a0c362f14c60a1c7f363e29"

API_TOKEN = '6037259563:AAEgHiJUvnYIWm0HDyfPrRexmi5OdOjRNYg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привіт!Я Бот-Синоптік!Напиши назву міста.")


@dp.message_handler(lambda message: message.text not in ["Фото","музика"])
async def echo(message: types.Message):
    r1 = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric")
    data = r1.json()
    city = data["name"]
    temperature = round(data["main"]["temp"])
    humidity = round(data["main"]["humidity"])
    wind = round(data["wind"]["speed"])
    await message.reply(f"***{datetime.datetime.now().strftime('%b %d %Y %H:%M')}***\n"
                        f"Погода в місті: {city}\n\U0001F321Температура: {temperature} C°\n"
                        f"\U0001F4A7Вологість повітря: {humidity} %\n"
                        f"\U0001F32AВітер: {wind} м/с\n ")
    
@dp.message_handler(regexp='Фото')
async def photo(message: types.Message):
    # await message.reply('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flypgs.com%2Fen%2Fcity-guide%2Fkyiv-travel-guide&psig=AOvVaw1i1TKsrJLDHONICwvwzzFT&ust=1681574577311000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMjwn8zfqf4CFQAAAAAdAAAAABAE')
    await bot.send_photo(chat_id=message.chat.id, photo=open('kiev.jpeg', 'rb'))


@dp.message_handler(regexp='музика')
async def photo(message: types.Message):
    await message.reply('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flypgs.com%2Fen%2Fcity-guide%2Fkyiv-travel-guide&psig=AOvVaw1i1TKsrJLDHONICwvwzzFT&ust=1681574577311000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMjwn8zfqf4CFQAAAAAdAAAAABAE')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
