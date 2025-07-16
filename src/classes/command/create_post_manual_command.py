from telegram import ParseMode
from .abstract.a_create_post_command import ACreatePostCommand

class CreatePostManualCommand(ACreatePostCommand):
    def __init__(self):
        super().__init__("create_post_manual", "🖋️ Create Post (Manual)")
    def run(self, update, context):
        message = update.message.text.replace("/post", "")
        if not message:
            update.message.reply_text("Formato non valido. Fornisci almeno un link")
            return 
        
        try:
            if ";" in message:
                args = [arg.strip() for arg in message.split(";")]
                if len(args) != 4:
                    update.message.reply_text("Formato non valido. Assicurati di fornire i dati nel seguente formato *nome ; prezzo ; image_url ; link*", parse_mode=ParseMode.MARKDOWN)
                    return 
                name, price, image_url, link = args
            else:
                link = message
                parsedLink = self._parse_link(link)
        except Exception as e:
            update.message.reply_text(f"Errore: {str(e)}")
        #      else:
        #         # Modalità solo link
        #         link = message
        #         parsed = self.parse_product(link)
        #         if not parsed:
        #             update.message.reply_text("Non sono riuscito a estrarre i dati dal link.")
        #             return
        #         name = parsed["name"]
        #         price = parsed["price"]
        #         image_url = parsed["image_url"]

        #     caption = f"🛍 <b>{name}</b>\n💸 Prezzo: <b>{price}</b>\n🔗 <a href='{link}'>Link al prodotto</a>"

        #     chiama la create_post che eredita dalla classe atratta di livello 2
                
    def __parse_link(link):
        print(link)