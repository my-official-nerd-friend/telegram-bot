import os
import logging
import requests
import schedule
import time
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

def controlla_offerte():
    print("Controllo offerte ora...")
    send_offer()  

schedule.every(1).hour.do(controlla_offerte)

while True:
    schedule.run_pending()
    time.sleep(1)