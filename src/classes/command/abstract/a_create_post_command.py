# This is the abstract class that every create post command
# has to extends in order to inherited the command's
# common attributes and functionalities

from telegram import ParseMode
from src.classes.command.abstract.a_command import ACommand

class ACreatePostCommand(ACommand):
    def create_post(self,context, channel_id, image_url, caption):
        context.bot.send_photo(
            chat_id=channel_id,
            photo=image_url,
            caption=caption,
            parse_mode=ParseMode.HTML
        )    
    