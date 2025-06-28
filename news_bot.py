from telebot import TeleBot
import pickle

TOKEN = 

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

bot = TeleBot(token = TOKEN)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, f"🤖 Բարև {message.from_user.first_name}")
    bot.reply_to(message, f"""📰 Ուղարկիր նորության հոդվածը և ես կորոշեմ նրա դասը։
    Այն կարող է վերաբերվել հետևյալ դասերին՝
        - Քաղաքական
        - Հասարակական
        - Կրթական
        - Առողջապահական""")

@bot.message_handler()
def classification_news(message):
    bot.send_message(message.chat.id, model.predict([message.text]))

bot.infinity_polling()