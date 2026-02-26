import os
import telebot
from google import genai
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")

# Eng yangi Google Gen AI mijozini sozlash
client = genai.Client(api_key=API_KEY)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Bot "yozmoqda..." holatini ko'rsatadi
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Gemini-ga so'rov yuborish
        response = client.models.generate_content(
            model="gemini-2.0-flash", # Eng oxirgi model versiyasi
            contents=message.text
        )
        
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        # Xatolikni Telegramga yuborish (muammoni ko'rish uchun)
        bot.reply_to(message, f"Xatolik chiqdi: {str(e)[:100]}")

print("Bot qayta ishga tushdi...")
bot.infinity_polling()
