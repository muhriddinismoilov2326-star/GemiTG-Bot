import os
import telebot
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Kalitlarni olish
TOKEN = os.getenv("TELEGRAM_TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")

# Yangi Gemini mijozini sozlash
client = genai.Client(api_key=API_KEY)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Foydalanuvchiga yozayotganini ko'rsatish
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Yangi formatda so'rov yuborish
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=message.text
        )
        
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        bot.reply_to(message, "Kechirasiz, hozir javob bera olmayman. API kalit yoki model bilan muammo bor.")

print("Bot 24/7 rejimida ishga tushdi...")
bot.infinity_polling()
