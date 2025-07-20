from src.classes.command.help_command import HelpCommand
from src.classes.command.create_post_manual_command import CreatePostManualCommand 

COMMANDS = {
    cmd.name: cmd
    for cmd in [HelpCommand(), CreatePostManualCommand()]
}