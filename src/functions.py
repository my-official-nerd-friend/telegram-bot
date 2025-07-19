from src.commands import COMMANDS

def handle_command_callback(update, context):
    query = update.callback_query
    query.answer()

    cmd_name = query.data
    if cmd_name:
        cmd = COMMANDS.get(cmd_name)
        if cmd:
            cmd.run(update, context)
        else:
            query.message.reply_text("❌ Comando non trovato.")