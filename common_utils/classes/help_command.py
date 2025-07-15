from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .command import Command

class HelpCommand(Command):
    def __init__(self):
        super().__init__("help", "❓ Help")
    def run(self, update, context):
        commands = context.bot_data.get("COMMANDS", {})
        keyboard = [
            [InlineKeyboardButton(cmd.label, callback_data=cmd.name)]
            for cmd in commands.values()
        ]
        return update.message.reply_text(
            "📋 Commands:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )