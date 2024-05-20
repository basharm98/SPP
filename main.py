import requests,telebot
import json
import time

tokenBot = input(' 7075082041:AAFo7fKTEgkD7-bQgmjbcmIH-Af_fjeKrmY ')

run = telebot.TeleBot(tokenBot)
@run.message_handler(commands = ['start'])
def Start(message):
    run.send_message(message.chat.id,text="* Hi Bro im * [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q) \n *Send* /gen *To Generation Visa !*",parse_mode="Markdown",disable_web_page_preview=True)
    

@run.message_handler(commands=["gen"])
def L7Ninfo_tik_tok(message):
	url = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
	cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    
	data = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    
	response = requests.post(url ,headers=headers , cookies=cookies,data=data).text
	data2 = json.loads(response)
	card = data2['creditCard'][1]
	a = card['IssuingNetwork']
	b = card['CardNumber']
	c = card['Bank']
	d = card['Name']
	e = card['Address']
	f = card['Country']
	h = card['CVV']
	i = card['Expiry']
	j = card['Pin']	
	sent_message=run.reply_to(message,text="Generating cards...")
	time.sleep(1)
	run.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id, text="""
*[-] Brand :* `{}`
*[-] Card Number :* `{}`
*[-] Bank :* `{}`
*[-] Name :* `{}`
*[-] Address :* `{}`
*[-] Country :* `{}` 🇺🇸
*[-] CVV :* `{}`
*[-] Expiry :* `{}`
*[-] Pin :* `{}`
*============================
[-] by :* [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q)   - @ToPython
    
    """.format(a,b,c,d,e,f,h,i,j),parse_mode="Markdown",disable_web_page_preview=True)

run.polling(True)    
