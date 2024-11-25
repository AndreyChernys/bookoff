from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
import random


routerl = Router()

from app.list import dragon_list
import app.links as ln



@routerl.message(F.text.lower() == 'открыть')
async def open1(message: Message):
  rand = random.choice(dragon_list)
  await message.reply_photo(photo=rand["photo"], caption=rand["text"], reply_markup=ln.open)


@routerl.message(Command('open'))
async def open2(message: Message):
  rand = random.choice(dragon_list)
  await message.reply_photo(photo=rand["photo"], caption=rand["text"], reply_markup=ln.open)

