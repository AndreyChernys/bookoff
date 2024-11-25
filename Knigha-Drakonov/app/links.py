from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)
from aiogram import Router

routerl = Router()




open = ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='Открыть')]
    ],
    resize_keyboard=True,
)

