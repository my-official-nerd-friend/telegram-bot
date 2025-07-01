import os
import logging
import requests
from dotenv import load_dotenv

# Carica le variabili da .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")

def get_amazon_product():
    return {
        'title': 'Echo Dot (5ª generazione)',
        'price': '29.99€',
        'link': 'https://google.com',
        'discount': '40%'
    }
    
def send_offer():
    product = get_amazon_product()
    message = (
        f"🔥 *Offerta Amazon!*\n\n"
        f"📦 *{product['title']}*\n"
        f"💸 Prezzo: {product['price']} (-{product['discount']})\n"
        f"🔗 [Acquista su Amazon]({product['link']})\n\n"
        f"_Questo link è affiliato._"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id" : TELEGRAM_CHANNEL,
        "text": message
    }
    r = requests.post(url, json=payload)
    print(r.json())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        logging.info("✅ Bot avviato - Invio offerta ora")
        send_offer()
    except Exception as e:
        logging.error(f"Errore: {e}")

'''
    import os

    import telebot

    # BOT_TOKEN = os.getenv('BOT_TOKEN')
    bot = telebot.TeleBot("6239740315:AAFKiR4EzT6crDldBKcPftSczpxPeOMpBGA")

    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    bot.infinity_polling()
'''