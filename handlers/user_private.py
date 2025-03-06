from aiogram import types, Router
from aiogram.filters import CommandStart, Command
import asyncio
import aiofiles
from idna import encode


user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Здравствуйте это виртуальный помощник. \n "
    "Я помогу вам сделать заказ =)")


@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")


@user_private_router.message(Command("feedback"))
async def feedback_cmd(message: types.Message):
    async with  aiofiles.open("feedback_cal.txt", "a", encoding="utf-8") as file:
        await file.write(f"Перезвонить {message.date}-{message.from_user.first_name}-{message.from_user.last_name}-{message.from_user.username}\n")

