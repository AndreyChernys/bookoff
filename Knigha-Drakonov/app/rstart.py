from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message




from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from sqlalchemy import select

rstartr = Router()
import app.links as ln


engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
  pass


class User(Base):
  __tablename__ = 'users'
  id: Mapped[int] = mapped_column(primary_key=True)
  tg_id = mapped_column(BigInteger, unique = True)
  first_name = mapped_column(String)
  username = mapped_column(String)




async def async_main():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)



async def set_user(tg_id, first_name, username):
  async with async_session() as session:
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    if not user:
      session.add(User(tg_id = tg_id, first_name = first_name, username = username))
      await session.commit()




@rstartr.message(Command('start'))
async def start(message: Message):
  if message.from_user:
    await set_user(message.from_user.id, message.from_user.first_name, message.from_user.username)
  await message.answer("Бот симулятор кейсов с драконами!\nНажмите 'Открыть' что бы открыть кейс!", reply_markup=ln.open)