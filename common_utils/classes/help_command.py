from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .a_command import ACommand

class HelpCommand(ACommand):
    def __init__(self):
        super().__init__("help", "❓ Help")
    def run(self, update, context):
        commands = context.bot_data.get("COMMANDS", {})
        
        tmp = []
        keyboard = []
        for i, cmd in enumerate(commands.values()):
            if i % 2 == 0 and i != 0:
                keyboard.append(tmp)
                tmp = []
            else:
                tmp.append(InlineKeyboardButton(cmd.label, callback_data=cmd.name)) 
        keyboard.append(tmp)
        return update.message.reply_text(
            "📋 Commands:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )