
from pyrogram import Client,filters,enums,idle
import redis ,requests,pytz,asyncio,threading
from datetime import datetime, timedelta
import time as T
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

api_id = 13296661
api_hash = "44d7de0b99917321d0db5d1572623208"
token = "7011787964:AAGtz2OGxQepIjt-DcoH5VPgJZBk09zxaBw"
bot_id = token.split(':')[0]
bot = Client("Azan_bot",api_id=api_id , api_hash=api_hash ,bot_token=token,in_memory=False)

async def Admin(msg) :
   admins = [6556354444]
   async for m in bot.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      admins.append(m.user.id)
   if (msg.from_user.id in admins) :
      return True
   else : 
      return False 

cairo_timezone = pytz.timezone('Africa/Cairo')
api_url = 'http://api.aladhan.com/v1/timingsByCity'

parameters = {
    'city': 'Cairo',
    'country': 'Egypt',
}

def get_prayer_times():
    try:
        data = requests.get(api_url, params=parameters).json()
        prayer_times = data['data']['timings']
        prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
        return {prayer: datetime.strptime(prayer_times[prayer], '%H:%M') for prayer in prayers}
    except Exception as e:
        print(f"Error retrieving prayer times: {e}")
        return None

async def send_prayer_notification(prayer, chats):
    prayer = prayer.replace('Fajr','الفجر').replace('Dhuhr','الظهر').replace('Asr','العصر').replace('Maghrib','المغرب').replace('Isha','العشاء')
    message = f'حان الآن موعد أذان {prayer} حسب التوقيت المحلي لمدينة القاهرة'
    for chat in chats:
        await bot.send_message(chat, message)

def Azann():
    last_update = None
    while True:
        current_time = datetime.now()
        if last_update is None or current_time.date() > last_update.date():
            prayer_times = get_prayer_times()
            if prayer_times:
                last_update = current_time
        chats = r.smembers(f'{bot_id}:azan_chats')
        if chats:
            for prayer, time in prayer_times.items():
                if current_time.strftime('%H:%M') == time.strftime('%H:%M'):
                    asyncio.run(send_prayer_notification(prayer, chats))
        T.sleep(50)

@bot.on_message(filters.command('تفعيل الاذان$','')&filters.group)
async def azan_on(c,msg):
    if not await Admin(msg) :
        return await msg.reply('• مرحبا {}\n• هذا الامر يخص مشرفين الجروب فقط',format(msg.from_user.mention))
    r.sadd(f'{bot_id}:azan_chats',msg.chat.id)
    await msg.reply('• مرحبا {}\n• تم تفعيل الاذان'.format(msg.from_user.mention))

@bot.on_message(filters.command('تعطيل الاذان$','')&filters.group)
async def azan_off(c,msg):
    if not await Admin(msg) :
        return await msg.reply('• مرحبا {}\n• هذا الامر يخص مشرفين الجروب فقط',format(msg.from_user.mention))
    r.srem(f'{bot_id}:azan_chats',msg.chat.id)
    await msg.reply('• مرحبا {}\n• تم تعطيل الاذان'.format(msg.from_user.mention))


bot.start()
print('\nBot started\nDev : @FPFFG')
Azan_thread = threading.Thread(target=Azann)
Azan_thread.start()
idle()
