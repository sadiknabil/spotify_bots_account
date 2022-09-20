import requests
from random import choice, randint
from string import ascii_letters, ascii_lowercase, digits

url = "https://spclient.wg.spotify.com/signup/public/v2/account/create"
domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'hotmail.fr', 'outlook.com', 'icloud.com', 'mail.com', 'live.com', 'yahoo.it', 'yahoo.ca', 'yahoo.in', 'live.se', 'orange.fr', 'msn.com', 'mail.ru', 'mac.com']
email = '%s@%s' % (''.join(choice(ascii_lowercase + digits) for _ in range(randint(7, 10))), choice(domains))
password = ''.join(choice(ascii_letters + digits) for _ in range(randint(8, 14)))

payload=f"{{\r\n    \"account_details\": {{\r\n        \"birthdate\": \"1989-06-12\",\r\n        \"consent_flags\": {{\r\n            \"eula_agreed\": true,\r\n            \"send_email\": false,\r\n            \"third_party_email\": false\r\n        }},\r\n        \"display_name\": \"nabiilspoty\",\r\n        \"email_and_password_identifier\": {{\r\n            \"email\": \"{email}\",\r\n            \"password\": \"Hz5QhfUBEnU6vfT\"\r\n        }},\r\n        \"gender\": 1\r\n    }},\r\n    \"callback_uri\": \"https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=fr\",\r\n    \"client_info\": {{\r\n        \"api_key\": \"a1e486e2729f46d6bb368d6b2bcda326\",\r\n        \"app_version\": \"v2\",\r\n        \"capabilities\": [\r\n            1\r\n        ],\r\n        \"installation_id\": \"5e10d26f-8843-422e-afd6-7ce417dd8eb5\",\r\n        \"platform\": \"www\"\r\n    }},\r\n    \"tracking\": {{\r\n        \"creation_flow\": \"\",\r\n        \"creation_point\": \"https://www.spotify.com/fr/\",\r\n        \"referrer\": \"\"\r\n    }}\r\n}}"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
  'Accept': '*/*',
  'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/json',
  'Origin': 'https://www.spotify.com',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'no-cors',
  'Sec-Fetch-Site': 'same-site',
  'Referer': 'https://www.spotify.com/',
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache'
}
print("call ")
response = requests.request("POST", url, headers=headers, data=payload)
print(response.json()['success']['username'])
print("end ")
print(response.text)
