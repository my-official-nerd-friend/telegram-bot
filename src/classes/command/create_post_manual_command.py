from telegram import ParseMode
import urllib.request
from .abstract.a_create_post_command import ACreatePostCommand

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
                if ";" in text:
                    args = [arg.strip() for arg in text.split(";")]
                    if len(args) != 3:
                        update.message.reply_text("Formato non valido. Assicurati di fornire i dati nel seguente formato *nome;prezzo;image_url*", parse_mode=ParseMode.MARKDOWN)
                        return 
                    name, price, image_url = args
                    print("3 input args: ", name, price, image_url)
                if text:
                    link = text
                    parsed = self.__parse_link(link)
                    if not parsed:
                        update.message.reply_text("Non sono riuscito a estrarre i dati dal link.")
                        return
                    name = parsed["name"]
                    price = parsed["price"]
                    image_url = parsed["image_url"]
                    print("3 link args: ", name, price, image_url)  
                if not text :
                    return update.message.reply_text("Formato non valido. Assicurati di fornire i dati nel seguente formato *nome;prezzo;image_url* oppure anche solo un *link*", parse_mode=ParseMode.MARKDOWN)
            except Exception as e:
                update.message.reply_text(f"Errore: {str(e)}")    
        if not update.callback_query and not update.message:
            return update.message.reply_text("Errore Generico")
        
        return

        # #     caption = f"🛍 <b>{name}</b>\n💸 Prezzo: <b>{price}</b>\n🔗 <a href='{link}'>Link al prodotto</a>"

        # #     chiama la create_post che eredita dalla classe atratta di livello 2
                
    def __parse_link(self,link):
        req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read() 
        strLink = data.decode("utf8")
        print(strLink)
        ## name : prendere la stringa dentro l'elemento con id productTitle
        ## prezzo : prendere la stringa dentro l'elemento con id corePriceDisplay_desktop_feature_div
        ## image_url : prendere l'src dentro l'elemento con id imgTagWrapperId
        return {
            "name": "Sample",
            "price": "2€",
            "image_url": "abc"
        }
        