import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")

import time
import schedule
from telegram.ext import Updater
from common_utils import Scheduler

# ---- Comando Telegram ----
# def start(update, context):
#     update.message.reply_text("Ciao! Sono attivo e ascolto i comandi.")

def hello():
    print("hello")

# ---- Avvio del bot ----
def main():
    
    scheduler = Scheduler()
    scheduler.schedule_task_in_seconds(5, hello)
    scheduler.start()

    # Avvio bot Telegram
    updater = Updater(BOT_TOKEN, use_context=True)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()