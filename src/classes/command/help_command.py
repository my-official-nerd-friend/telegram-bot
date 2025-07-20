from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from src.classes.command.abstract.a_command import ACommand
from src.constants import MAX_COMMANDS_PER_LINE

class HelpCommand(ACommand):
    def __init__(self):
        super().__init__("help", "❓ Help")
    def run(self, update, context):
        commands = context.bot_data.get("COMMANDS", {})
        
        tmp = []
        keyboard = []
        for i, cmd in enumerate(commands.values()):
            if i % MAX_COMMANDS_PER_LINE == 0 and i != 0:
                keyboard.append(tmp)
                tmp = []
            else:
                tmp.append(InlineKeyboardButton(cmd.label, callback_data=cmd.name)) 
        keyboard.append(tmp)
        
        message = update.message or update.callback_query.message
        return message.reply_text(
            "📋 Comandi:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )