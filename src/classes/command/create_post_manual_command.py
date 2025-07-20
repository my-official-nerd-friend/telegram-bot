from telegram import ParseMode
import html
from src.constants import AMAZON_AFFILIATE_TAG, TELEGRAM_CHANNEL
from src.classes.command.abstract.a_create_post_command import ACreatePostCommand
from src.functions.affiliate_link import get_amazon_affiliate_url, parse_link

class CreatePostManualCommand(ACreatePostCommand):
    def __init__(self):
        super().__init__("create_post_manual", "🖋️ Create Post (Manual)")
    def run(self, update, context):
        # situazione 1 : premo il comando dal menu di help
        if update.callback_query:
            update.callback_query.message.reply_text( 
                "\nInserisci il comando in questo modo: \n"                                     
                "<b><code>/create_post_manual</code></b>"
                " <i>nome;prezzo;link_immagine</i> oppure inserisci soltanto <i>link</i> ",
                parse_mode=ParseMode.HTML
            )      
        # situazione 2 : inserisco il comando da input
        if update.message:
            text = update.message.text.replace(f"/{self.name}", "")
            try:
                if not text :
                    return update.message.reply_text("Formato non valido. Assicurati di fornire i dati nel seguente formato *nome;prezzo;image_url* oppure anche solo un *link*", parse_mode=ParseMode.MARKDOWN)
                if ";" in text:
                    args = [arg.strip() for arg in text.split(";")]
                    print(args)
                    if len(args) != 4:
                        update.message.reply_text("Formato non valido. Assicurati di fornire i dati nel seguente formato *nome;prezzo;image_url*", parse_mode=ParseMode.MARKDOWN)
                        return 
                    name, price, image_url, link = args
                else:
                    link = text
                    parsed = parse_link(link)
                    if not parsed:
                        update.message.reply_text("Non sono riuscito a estrarre i dati dal link.")
                        return
                    name = parsed["name"]
                    price = parsed["price"]
                    image_url = parsed["image_url"]
                    
                affiliateLink = get_amazon_affiliate_url(link, AMAZON_AFFILIATE_TAG)
                caption = f"🛍 <b>{html.escape(name)}</b>\n💸 Prezzo: <b>{html.escape(price)}</b>\n🔗 <a href=\"{affiliateLink}\">Link al prodotto</a>"
                return self.create_post(context, TELEGRAM_CHANNEL, image_url, caption)
            except Exception as e:
                update.message.reply_text(f"Errore: {str(e)}")    
        if not update.callback_query and not update.message:
            return update.message.reply_text("Errore Generico")           