import telebot
import random

TOKEN = "7657302784:AAFKTW0VYDpY66U0Jz3X1qJzrprAkKEjQ1M"
bot = telebot.TeleBot(TOKEN)

users = {}

def load_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

quotes = load_quotes()

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Salom! Iltimos, ismingizni kiriting:")
    bot.register_next_step_handler(message, save_name)

def save_name(message):
    chat_id = message.chat.id
    users[chat_id] = message.text
    bot.send_message(chat_id, f"Rahmat, {message.text}! Motivatsiya olish uchun /motivate buyrug'idan foydalaning.")

@bot.message_handler(commands=["setname"])
def set_name(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Yangi ismingizni kiriting:")
    bot.register_next_step_handler(message, save_name)

@bot.message_handler(commands=["motivate"])
def motivate(message):
    chat_id = message.chat.id
    name = users.get(chat_id, "Do'stim")
    quote = random.choice(quotes)
    bot.send_message(chat_id, f"{name}, {quote}")

print("✅ Bot ishga tushdi...")

bot.polling()

print("❌ Bot toxtatildi... ")