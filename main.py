import telebot
import requests,os
from bs4 import BeautifulSoup

token = "6995501333:AAG29tC7PpoFq7l6a-B1SvY3jMRILMmGaos"
bot = telebot.TeleBot(token)

    
@bot.message_handler(commands=["start"])
def start(message):
	name = message.from_user.first_name
	user = message.from_user.username
	user = user.replace('@', '')
	url = 'https://t.me/'+user
	req = requests.get(url).text
	soup = BeautifulSoup(req, 'html.parser')
	photo = soup.find('meta', property="og:image")['content']
	bio = soup.find('meta', property="og:description")['content']

	id = message.from_user.id

	lan = message.from_user.language_code
	msg = bot.send_photo(message.chat.id, photo, caption=f'<b>▪ Nick: @{user}\n▪ ID: {id}\n▪ First: {name}\n▪️Bio : {bio}\n▪️ Lang: {lan}\n▪Deve : @ttxxxn</b>',parse_mode="HTML")	

@bot.message_handler(func=lambda message: True)
def all(message):
	name = message.from_user.first_name
	bot.reply_to(message,f'What, {name}')


bot.infinity_polling()