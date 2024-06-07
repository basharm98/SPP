from pyrogram import Client
import pyrogram
import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 25829176  # app id الخاص بك.
api_hash = "160b2bf653ee7dd974bd6d09a7968cd1"  # app hash
token="7298923155:AAEbILv5NVeQjmgmei_ldTIqWznk_tuVnIk"
# Create a new bot session
app = Client("gmm", api_id, api_hash, bot_token=token)

# Add your bot's logic here
@app.on_chat_member_updated()
def handle_message(lient, update):
    if update.old_chat_member:
        user_id = update.from_user.id
        chat_id = update.chat.id
        url = f"https://api.telegram.org/bot{token}/kickChatMember"
        params = {
         "chat_id": chat_id,
         "user_id": user_id
         }

        response = requests.get(url, params=params)
@app.on_message(filters.command("start"))
def start(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("hms", url="https://t.me/hms_01")],
        [InlineKeyboardButton("قناة البوت", url="https://t.me/botatiiii")]
    ])
    message.reply_text(
        "اهلين فيك في بوت حبيب المغادرين من القنوات 🦋\n\n"
        "كل ماعليك فعله اضافة البوت ادمن في القناه وسيتم التفعيل تلقائيا وسيتم حظر اي شخص غادر من قناتك ♡",
        reply_markup=reply_markup
    )



app.run()