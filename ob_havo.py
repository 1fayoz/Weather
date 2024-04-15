API_KEY = "f78c1bf5534ebc2b1cf973bb8023de3a"
# #status code 200:ok , 404: not found , 500:api da hato bor 403: ruxsat yoq, yoki eskirgan

import requests
from pprint import pprint
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
import logging

bot = Bot(token="6303342957:AAHEMGbxY_2Iezz_EXaBIH7rs8KSBIDxnpY")
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)



def reyly_button():
    buttons = [
        [KeyboardButton(text="Ob-havo malumotlari")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # pprint(data)
        latitude = data['coord']['lat']
        langitude = data['coord']['lon']
        namkil = data['main']['humidity']
        temprature = data ['main']['temp'] - 273
        city_name  = data ['name']
        country = data['sys']['country']
        weather = data['weather'][0]['main']
        wind_speed = data['wind']['speed']

        text = f"{city_name}({country}) \n  issiqlik darajasi: {temprature} \n OB-Havo holat: {weather} \n Namlik: {namkil} \n Shamol tezligi: {wind_speed} "
        return text, langitude, latitude


# print(weather_data('Toshkent'))


@dp.message(Command('start'))
async def start_button(message: Message):
    print(message.chat.id)
    await message.answer(text="Assalomu alaykum", reply_markup= reyly_button())

@dp.message(lambda message: message.text == "Ob-havo malumotlari")
async def weather_data1(message: Message):
    await message.answer(text="Shaxar nomini kiriitng")
@dp.message()
async def result(message: Message):
    city = message.text
    text = weather_data(city)

    await bot.send_location(chat_id=message.chat.id, 
    latitude=text[1],
    longitude=text[2]
    )
    await message.answer(text=text[0])


async def main():
    print("WORKING")
    # dp.include_router(form_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())





