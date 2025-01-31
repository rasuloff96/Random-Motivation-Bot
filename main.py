import os
import random
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# .env faylini yuklash
load_dotenv()

# Telegram bot tokeni
TOKEN = os.getenv("BOT_TOKEN")

# Logger sozlamalari
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Motivatsion gaplarni fayldan o‘qish
def load_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

quotes = load_quotes()

# /start buyrug'ini qayta ishlash
async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("💬 Get Motivation!", callback_data="motivation")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello! I am your motivational bot. Press the button or type /motivation to get inspired!",
        reply_markup=reply_markup
    )

# Tasodifiy motivatsion gap yuborish
async def send_motivation(update: Update, context):
    chat_id = update.effective_chat.id
    quote = random.choice(quotes)
    await context.bot.send_message(chat_id=chat_id, text=f"✨ {quote}")

# Tugma bosilganda motivatsiya yuborish
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    if query.data == "motivation":
        quote = random.choice(quotes)
        await query.message.reply_text(f"✨ {quote}")

# Botni ishga tushirish
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("motivation", send_motivation))
    application.add_handler(CallbackQueryHandler(button_callback))

    application.run_polling()

if __name__ == "__main__":
    main()
