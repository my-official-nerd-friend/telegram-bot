from src.classes import HelpCommand, CreatePostManualCommand

COMMANDS = {
    cmd.name: cmd
    for cmd in [HelpCommand(), CreatePostManualCommand()]
}