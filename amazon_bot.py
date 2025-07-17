from dotenv import load_dotenv 
load_dotenv()

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from src import Scheduler, BOT_TOKEN, COMMANDS, handle_command_callback

def main():
    
    scheduler = Scheduler()
    #scheduler.schedule_task_in_seconds(5, sample)
    scheduler.start()

    updater = Updater(BOT_TOKEN, use_context=True)
    updater.dispatcher.bot_data["COMMANDS"] = COMMANDS
    
    for cmd in COMMANDS.values():
        updater.dispatcher.add_handler(CommandHandler(cmd.name, cmd.run))
    updater.dispatcher.add_handler(CallbackQueryHandler(handle_command_callback))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()