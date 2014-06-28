from __future__ import print_function
import requests
import threading
import sys

global count
count = 0

class creis(object):
    def __init__(self):
        global count
        self.session = requests.session()
        while True:
            try:
                account = self.createAccount()
                if account['json']['success'] == 1:
                    count += 1
                    sys.stdout.write("\rAccounts Made: %d"%count)
                    print("%s:%s"%(account['user'], account['pass']), file=open("accounts", 'a'))
            except:
                continue

    def createAccount(self):
        username = self.generateUsername()
        self.register = self.session.post("http://creis.us/public/ajax/sign_up.php",
                                        data={
                                                'full_name': 'obnoxious',
                                                'username': '%s'%username,
                                                'email': '%s@mailnesia.com'%username,
                                                'password': 'gauhga',
                                                'captcha': 1337, #Static because the captcha check is clientsided LMFAO
                                                'terms': 1
                                             },
                                        headers={
                                            'Referer': 'http://creis.us/',
                                            'Cache-Control': 'no-cache',
                                            'Pragma': 'no-cache',
                                            'Accept-Encoding': 'gzip, deflate',
                                            'Accept-Language': 'en-US,en;q=0.5',
                                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                                        })
        return { 'json': self.register.json(), 'user': username, 'pass': 'gauhga' }

    def generateUsername(self):
        badList = [ "nigger", "cancer", "cum","gay","negro",
                    "homo","dirty","semen","hitler","jew","anus","jizz",
                    "pussy","penis","pussie","terror",
                    "terrorist","stinky",
                    "poo","dump","cunt","dick","lick",
                    "p3nis","urin","crack","fart",
                    "pusy","pubic","jerk","skeet",
                    "wank","pantie","skank","fuck",
                    "n1gg3r","fuk","skunk","jesus",
                    "bitch","cherry","b1tch","milf",
                    "hoe","tits","whore","ass",
                    "as5","white","black","bible",
                    "koran","butt","nipple","hair",
                    "dik","orgasm","vagina","pr0n",
                    "pron","porn","p0rn","www","fuc","d1ck","l1ck",
                    "bl0w","phuck","fcuk","fuuk","douch",
                    "cok","osama","piss","mum","mom","semen","ball","cameltoe","bone",
                    "suck","fuk","liks",
                    "b4ll","aids","an4l","lube","lu8e","rape","satan","p3nis","weiner",]
        while True:
            httpResponse = requests.get("http://www.gamertagcreator.com/ajax-suggestion-refresh.php")
            userName = httpResponse.text.split()[0].split()[0].lower()

            if "+" in userName:
                userName = "%s" % (userName.split('+')[0])

            if len(userName) < 4 or len(userName) >=25:
                continue

            for bad in badList:
                if bad in userName:
                    continue

            return userName

if __name__ == "__main__":
    for i in range(10):
        threading.Thread(target=creis).start()