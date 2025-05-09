from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from modules import osint_tools

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(
        "OSINT Bot Activated. Available commands: /email, /ip, /user, /domain"
    )

@dp.message_handler(commands=['email'])
async def email_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /email someone@example.com")
        return
    result = osint_tools.lookup_email(parts[1])
    await message.reply(result)
@dp.message_handler(commands=['phone'])
async def phone_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /phone +123456789")
        return
    result = osint_tools.lookup_phone(parts[1])
    await message.reply(result)

@dp.message_handler(commands=['tgid'])
async def tgid_handler(message: types.Message):
    user = message.from_user
    result = osint_tools.lookup_telegram_id(user.id)
    await message.reply(result)

@dp.message_handler(commands=['darknet'])
async def darknet_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /darknet keyword")
        return
    result = osint_tools.lookup_darknet(parts[1])
    await message.reply(result)

@dp.message_handler(commands=['report'])
async def report_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /report target")
        return
    result = osint_tools.generate_report(parts[1])
    await message.reply(result)

@dp.message_handler(commands=['ip'])
async def ip_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /ip 1.2.3.4")
        return
    result = osint_tools.lookup_ip(parts[1])
    await message.reply(result)

@dp.message_handler(commands=['user'])
async def user_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /user username")
        return
    result = osint_tools.lookup_username(parts[1])
    await message.reply(result)

@dp.message_handler(commands=['domain'])
async def domain_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /domain example.com")
        return
    result = osint_tools.lookup_domain(parts[1])
    await message.reply(result)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
