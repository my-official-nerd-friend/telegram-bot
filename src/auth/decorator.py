from functools import wraps
from src.constants import ALLOWED_CHAT_IDS
from datetime import datetime

def require_authorized_user(func):
    @wraps(func)
    def wrapper(self, update, context, *args, **kwargs):
        chat_id = update.effective_chat.id
        if f"{chat_id}" not in ALLOWED_CHAT_IDS:
            # potrei anche fare la stampa sul database locale...
            print(f"⚠️\tAccesso negato per chat_id: {chat_id} in data {datetime.now()}\t⚠️")
            update.message.reply_text(f"❗\tAccesso negato\t❗")
            return
        return func(self, update, context, *args, **kwargs)
    return wrapper