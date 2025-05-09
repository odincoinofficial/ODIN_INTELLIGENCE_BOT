from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from modules import osint_tools
from modules.pdf_generator import generate_pdf_report

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(
        "ODIN Bot Activated. Use /email /ip /domain /user /phone /tgid /darknet /report /pdfreport"
    )

@dp.message_handler(commands=['pdfreport'])
async def pdfreport_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("Usage: /pdfreport target@example.com")
        return
    query = parts[1]
    email = osint_tools.lookup_email(query)
    ip = osint_tools.lookup_ip(query)
    domain = osint_tools.lookup_domain(query)
    user = osint_tools.lookup_username(query)

    filename = generate_pdf_report(query, email, ip, domain, user)
    with open(filename, "rb") as doc:
        await message.reply_document(doc)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
