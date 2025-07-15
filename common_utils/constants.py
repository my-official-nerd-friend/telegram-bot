import os

from common_utils.classes import HelpCommand


#from common_utils.classes.help_command import HelpCommand

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")
COMMANDS = {
    cmd.name: cmd
    for cmd in [HelpCommand()]
}