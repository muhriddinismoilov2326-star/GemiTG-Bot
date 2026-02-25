import os
import telebot
import google.generativeai as genai
from dotenv import load_dotenv # Kalitlarni o'qish uchun kerak

# .env faylini kompyuter xotirasiga yuklaymiz
load_dotenv()

# Kalitlarni o'zgaruvchilarga biriktiramiz
TOKEN = os.getenv("TELEGRAM_TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini va Botni ishga tushiramiz
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply(message):
    response = model.generate_content(message.text)
    bot.reply_to(message, response.text)

print("Bot ishlamoqda...")
bot.infinity_polling()
