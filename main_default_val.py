from sys import stdout
from requests import post
from os import system, _exit, path
from random import choice, randint
from colors import green, red, reset
from time import time, sleep, strftime, gmtime
from threading import Thread, Lock, active_count
from string import ascii_letters, ascii_lowercase, digits

system('cls && title [Spotify Account Creator] - Main Menu')
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
domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'hotmail.fr', 'outlook.com', 'icloud.com', 'mail.com', 'live.com', 'yahoo.it', 'yahoo.ca', 'yahoo.in', 'live.se', 'orange.fr', 'msn.com', 'mail.ru', 'mac.com']
lock = Lock()

class Main:
    def __init__(self):
        self.variables = {
            'proxies': [],
            'proxy_num': 0,
            'created': 0,
            'retries': 0,
            'cpm': 0,
            'unlimited': False
        }

        logo = '''                                            ____ ___  ____ ___ _ ____ _   _       
                                            [__  |__] |  |  |  | |___  \_/        
                                            ___] |    |__|  |  | |      |         
                                      ____ ____ _  _ ____ ____ ____ ___ ____ ____ 
                                      | __ |___ |\ | |___ |__/ |__|  |  |  | |__/ 
                                      |__] |___ | \| |___ |  \ |  |  |  |__| |  \ '''

        print('%s%s' % (green(), logo))

        self.proxy_type = 'socks5'

        self.amount = '50'
        print()

        if self.amount == '':
            self.variables['unlimited'] = True
            self.amount = 0
        elif self.amount != '' and not self.amount.isdigit():
            print('%s> %sInvalid input%s.' % (reset(), red(), reset()))
            system('title [Spotify Account Creator] - Exiting . . .')
            sleep(3)
            _exit(0)

    def setup(self):
        if path.exists('Proxies.txt'):
            with open('Proxies.txt', 'r', encoding = 'UTF-8') as f:
                for line in f.read().splitlines():
                    if line != '':
                        self.variables['proxies'].append(line)
            if len(self.variables['proxies']) == 0:
                self.error_import(False)
        else:
            self.error_import(True)

    def error_import(self, create):
        if create:
            open('Proxies.txt', 'a').close()
        print('%s> %sPaste your proxies inside Proxies.txt%s!' % (reset(), red(), reset()))
        system('title [Spotify Account Creator] - Exiting . . .')
        sleep(3)
        _exit(0)

    def write(self, arg):
        lock.acquire()
        stdout.flush()
        stdout.write('%s\n' % (arg.encode('ascii', 'replace').decode())) # Get less printing bugs on Windows
        lock.release()

    def cpm_counter(self):
        if self.variables['unlimited']:
            while True:
                old = self.variables['created']
                sleep(4)
                new = self.variables['created']
                self.variables['cpm'] = ((new - old) * 15)
        else:
            while self.variables['created'] != int(self.amount):
                old = self.variables['created']
                sleep(4)
                new = self.variables['created']
                self.variables['cpm'] = ((new - old) * 15)

    def update_title(self):
        if self.variables['unlimited']:
            while True:
                elapsed = strftime('%H:%M:%S', gmtime(time() - self.start))
                system('title [Spotify Account Creator] - Created: %s ^| Retries: %s ^| CPM: %s ^| Time Elapsed: %s ^| Threads: %s' % (self.variables['created'], self.variables['retries'], self.variables['cpm'], elapsed, (active_count() - 2)))
                sleep(0.4)
        else:
            while self.variables['created'] != int(self.amount):
                elapsed = strftime('%H:%M:%S', gmtime(time() - self.start))
                system('title [Spotify Account Creator] - Created: %s/%s ^| Retries: %s ^| CPM: %s ^| Time Elapsed: %s ^| Threads: %s' % (self.variables['created'], self.amount, self.variables['retries'], self.variables['cpm'], elapsed, (active_count() - 2)))
                sleep(0.4)

            elapsed = strftime('%H:%M:%S', gmtime(time() - self.start))
            system('title [Spotify Account Creator] - Created: %s/%s ^| Retries: %s ^| CPM: %s ^| Time Elapsed: %s ^| Threads: %s' % (self.variables['created'], self.amount, self.variables['retries'], self.variables['cpm'], elapsed, (active_count() - 2)))

    def retry(self):
        self.variables['retries'] += 1
        self.creator(choice(self.variables['proxies']))

    def creator(self, proxy):
        email = '%s@%s' % (''.join(choice(ascii_lowercase + digits) for _ in range(randint(7, 10))), choice(domains))
        password = 'Hz5QhfUBEnU6vfT'
        birth_year = randint(1970, 2005)
        birth_month = randint(1, 12)
        birth_day = randint(1, 28)
        gender = choice(['male', 'female'])

        payload=f"{{\r\n    \"account_details\": {{\r\n        \"birthdate\": \"1989-06-12\",\r\n        \"consent_flags\": {{\r\n            \"eula_agreed\": true,\r\n            \"send_email\": false,\r\n            \"third_party_email\": false\r\n        }},\r\n        \"display_name\": \"nabiilspoty\",\r\n        \"email_and_password_identifier\": {{\r\n            \"email\": \"{email}\",\r\n            \"password\": \"Hz5QhfUBEnU6vfT\"\r\n        }},\r\n        \"gender\": 1\r\n    }},\r\n    \"callback_uri\": \"https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=fr\",\r\n    \"client_info\": {{\r\n        \"api_key\": \"a1e486e2729f46d6bb368d6b2bcda326\",\r\n        \"app_version\": \"v2\",\r\n        \"capabilities\": [\r\n            1\r\n        ],\r\n        \"installation_id\": \"5e10d26f-8843-422e-afd6-7ce417dd8eb5\",\r\n        \"platform\": \"www\"\r\n    }},\r\n    \"tracking\": {{\r\n        \"creation_flow\": \"\",\r\n        \"creation_point\": \"https://www.spotify.com/fr/\",\r\n        \"referrer\": \"\"\r\n    }}\r\n}}"
        
        try:
            create = post('https://spclient.wg.spotify.com/signup/public/v2/account/create', data = payload, headers = headers)
            if create.json()['success'] is not None:
                username = create.json()['success']['username']
                if username != '':
                    self.write('%s[%sCREATED%s] %s:%s | Username: %s | Gender: %s | Date of Birth: %s/%s-%s' % (green(), reset(), green(), email, password, username, gender.replace(gender[0], gender[0].upper()), birth_day, birth_month, birth_year))
                    with open('Created [RAW].txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s\n' % (email, password))
                    with open('Created [CAPTURE].txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s | Username: %s | Gender: %s | Date of Birth: %s/%s-%s\n' % (email, password, username, gender.replace(gender[0], gender[0].upper()), birth_day, birth_month, birth_year))

                    self.variables['created'] += 1
                else:
                    self.retry()
            else:
                self.retry()
        except:
            self.retry()

    def multi_threading(self):
        self.start = time()
        Thread(target = self.cpm_counter).start()
        Thread(target = self.update_title).start()

        if self.variables['unlimited']:
            while True:
                try:
                    Thread(target = self.creator, args = (self.variables['proxies'][self.variables['proxy_num']],)).start()
                except:
                    continue
                self.variables['proxy_num'] += 1
                if self.variables['proxy_num'] >= len(self.variables['proxies']):
                    self.variables['proxy_num'] = 0
        else:
            num = 0
            while num < int(self.amount):
                try:
                    Thread(target = self.creator, args = (self.variables['proxies'][self.variables['proxy_num']],)).start()
                except:
                    continue
                num += 1
                self.variables['proxy_num'] += 1
                if self.variables['proxy_num'] >= len(self.variables['proxies']):
                    self.variables['proxy_num'] = 0
            
            while self.variables['created'] != int(self.amount):
                continue
            print('\n%s> %sFinished%s.' % (reset(), green(), reset()))
            system('pause >NUL')
            print('> Exiting . . .')
            sleep(3)
            _exit(0)

if __name__ == '__main__':
    main = Main()
    main.setup()
    main.multi_threading()
