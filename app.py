from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
import os


bot = Bot(token=os.getenv("TG_TOKEN"))

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это была команда старт")


@dp.message()
async def echo(message: types.Message):
    await message.answer(f"{message.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
