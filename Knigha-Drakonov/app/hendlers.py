from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()




@router.message(Command('help'))
async def help(message: Message):
  await message.answer("По вопросам обращаться к менеджеру проэкта @gerahomeoff")


@router.message(Command('site'))
async def site(message: Message):
  await message.answer("Про проэкт можно посмотреть в ТГ канале @book_of_dragon_news")




