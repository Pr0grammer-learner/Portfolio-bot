import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

class TelegramBot():
    def __init__(self, token : str):
        self.TOKEN = token
        self.dp = Dispatcher()
        self.bot = Bot(token=self.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.setup_handlers()
        
    def setup_handlers(self):
        @self.dp.message(CommandStart())
        async def command_start_handler(message: Message) -> None:
            await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! Этот бот создан, как интерактивное портфолио Привалова Тимофея Александровича!")

    async def run(self):
        await self.dp.start_polling(self.bot)

   

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    load_dotenv()
    TOKEN = getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("BOT_TOKEN is not defined")
    bot = TelegramBot(token=TOKEN)
    asyncio.run(bot.run())
    