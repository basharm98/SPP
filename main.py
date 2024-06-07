import telebot

bot = telebot.TeleBot("7232595306:AAEzFZm7s2zbKFzoRmSnWC0VSoVMmlWl7dk")


play_song_button = telebot.types.InlineKeyboardButton('استماع لأغنية', callback_data='play_song')


next_button = telebot.types.InlineKeyboardButton('التالي', callback_data='next')


main_keyboard = telebot.types.InlineKeyboardMarkup()
main_keyboard.add(play_song_button)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'add_song':
        if call.message.chat.id == 7246248054:
            bot.send_message(call.message.chat.id, "يرجى إرسال الأغنية التي تريد إضافتها.")
        else:
            bot.send_message(call.message.chat.id, "ليس لديك الصلاحية لإضافة أغاني.", reply_markup=main_keyboard)
    elif call.data == 'play_song':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(next_button)
        audio = open('song.mp3', 'rb')
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio, reply_markup=keyboard)
    elif call.data == 'next':
        audio = open('song2.mp3', 'rb')
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.edit_message_media(media=telebot.types.InputMediaAudio(audio), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=main_keyboard)

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    if message.from_user.id == 7246248054:
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('song.mp3', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, "تم إضافة الأغنية بنجاح!", reply_markup=main_keyboard)
    else:
        bot.send_message(message.chat.id, "ليس لديك الصلاحية لإضافة أغاني.", reply_markup=main_keyboard)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
 
    developer_keyboard = telebot.types.InlineKeyboardMarkup()
    add_song_button = telebot.types.InlineKeyboardButton('إضافة أغنية', callback_data='add_song')
    developer_keyboard.add(add_song_button, play_song_button)

    if message.from_user.id == 7246248054:
        bot.send_message(message.chat.id, "مرحباً بك في بوت الأغاني! يرجى استخدام الأزرار للاستماع للأغاني.", reply_markup=developer_keyboard)
    else:
        bot.send_message(message.chat.id, "مرحباً بك في بوت الأغاني! يرجى استخدم الأزرار للاستماع للأغاني.", reply_markup=main_keyboard)




bot.polling()