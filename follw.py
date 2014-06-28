from __future__ import print_function
import requests
import threading
import sys
from time import sleep

global count
count = 0

class follow(object):
    def __init__(self, username):
        global count
        self.username = username
        self.target = sys.argv[1]
        for i in range (3):
            try:
                self.session = requests.session()
                if "True" in self.login():
                    pass
                else:
                    return
                self.dataId = self.session.get("http://creis.us/%s"%self.target).text.split('<span data-username="devin"')[1].split('data-id="')[1].split('"')[0]
                if self.follow().json()['status'] == 1:
                    count += 1
                    sys.stdout.write("\rFollows Sent: %d"%count)
            except:
                continue

    def follow(self):
        return self.session.post("http://creis.us/public/ajax/follow.php", data={'id': self.dataId})

    def login(self):
        return self.session.post("http://creis.us/public/ajax/sign_in.php", data={'user': self.username, 'password': 'gauhga'})

if __name__ == "__main__":
    for account in open("accounts", 'r').readlines():
        threading.Thread(target=follow, args=[account.strip().split(":")[0]]).start()
        sleep(0.5)