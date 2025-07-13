from dotenv import load_dotenv
load_dotenv()

from telegram.ext import Updater
from common_utils import Scheduler, TELEGRAM_CHANNEL, BOT_TOKEN

# ---- Comando Telegram ----
# def start(update, context):
#     update.message.reply_text("Ciao! Sono attivo e ascolto i comandi.")

def sample():
    print("this is a sample message")

# ---- Avvio del bot ----
def main():
    
    scheduler = Scheduler()
    scheduler.schedule_task_in_seconds(5, sample)
    scheduler.start()

    # Avvio bot Telegram
    updater = Updater(BOT_TOKEN, use_context=True)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()