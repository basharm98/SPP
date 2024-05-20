import requests
import telebot
from telebot.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Mak

token = "6995501333:AAG29tC7PpoFq7l6a-B1SvY3jMRILMmGaos"
bot = telebot.TeleBot(token)

sent_video_messages = {}

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, 'ارسل رابط فيديو على الانستقرام')

@bot.message_handler(content_types=['text'])
def Down(message):
    try:
    	link = message.text
    	json_data = {
    	    'url': link
    	}
    	response = requests.post('https://insta.savetube.me/downloadPostVideo', json=json_data).json()
    	thu = response['post_video_thumbnail']
    	video = response['post_video_url']
    	
    	sent_message = bot.send_photo(message.chat.id, thu, reply_to_message_id=message.message_id, reply_markup=Mak().add(Btn('تحميل الفيديو', callback_data='vid')))
    	
    	sent_video_messages[sent_message.message_id] = video
    except:
    	bot.reply_to(message,'Invalid link')

@bot.callback_query_handler(func=lambda call: call.data == 'vid')
def all(call):
    message_id = call.message.message_id
    if message_id in sent_video_messages:
        video = sent_video_messages[message_id]
        
        bot.delete_message(call.message.chat.id, call.message.message_id)
        Mn = f"[تم تحميل بواسطة](ttxxxn.t.me)"
        bot.send_video(call.message.chat.id,video,caption=Mn,parse_mode="Markdown")
        
bot.infinity_polling()