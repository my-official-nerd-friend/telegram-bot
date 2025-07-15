from common_utils.classes import HelpCommand, CreatePostManualCommand

COMMANDS = {
    cmd.name: cmd
    for cmd in [HelpCommand(), CreatePostManualCommand()]
}