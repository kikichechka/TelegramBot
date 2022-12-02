from aiogram import Bot, Dispatcher, executor, types
import logging
import time
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
my_token = os.getenv('TOKEN')
my_weather_token = os.getenv('WEATHER_TOKEN')

app = Bot(token=my_token)
dp = Dispatcher(app)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    filename='my_log.log'
)


@dp.message_handler(Text("Погода"))
async def where(message: types.Message):
    urlkb = InlineKeyboardMarkup(row_width=1)
    urlButton1 = InlineKeyboardButton(text='Yandex погода', url="https://yandex.ru/pogoda/")
    urlButton2 = InlineKeyboardButton(text='Qismeteo', url="https://www.gismeteo.ru/")
    urlButton3 = InlineKeyboardButton(text='AccuWeather', url="https://www.accuweather.com/")
    urlkb.add(urlButton1, urlButton2, urlButton3)
    await message.answer('Выберите сервис:' ,reply_markup=urlkb)

@dp.message_handler(Text("Дата и время"))
async def where(message: types.Message):
    date_now = time.strftime("%d/%m/%Y")
    time_now = time.strftime("%H:%M:%S")
    await message.answer(f'Текущая дата: {date_now}\nТекущее время: {time_now}')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.InlineKeyboardButton(text="Дата и время"),
           types.InlineKeyboardButton(text="Погода"),
           types.InlineKeyboardButton(text="Запросить геолокацию", request_location=True)
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите действие:")
   await message.answer(f"Привет {message.from_user.first_name}!\nЯ уникальный бот!\nВыбери действие, а я тебе обязательно отвечу.", reply_markup=keyboard)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
