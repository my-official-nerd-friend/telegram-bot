# This is the abstract class that every create post command
# has to extends in order to inherited the command's
# common attributes and functionalities

from telegram import ParseMode
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from src.classes.command.abstract.a_command import ACommand

class ACreatePostCommand(ACommand):
    def create_post(self,context, channel_id, image_url, caption):
        context.bot.send_photo(
            chat_id=channel_id,
            photo=image_url,
            caption=caption,
            parse_mode=ParseMode.HTML
        )
    def get_amazon_affiliate_url(self, link, my_tag):
        parsed = urlparse(link)
        qs = parse_qs(parsed.query)
        qs['tag'] = my_tag
        new_q = urlencode(qs, doseq=True)
        return urlunparse(parsed._replace(query=new_q)).strip()     
    