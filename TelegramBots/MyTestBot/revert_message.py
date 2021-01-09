import requests
import sys
import json
import time

bot_url = "https://api.telegram.org/bot1508990442:AAE40vSWEBgww1siZ5GJnxQbxfOFX0SezME/"

class Bot:
    def __init__(self):
        self._offset = None

    def getLastUpdate(self):
        ploads = {'limit':1, "offset": self._offset}
        r = requests.get(bot_url + "getUpdates", params=ploads)
        if (r.status_code != 200):
            print(r.status_code)
            return False

        f = open("demofile.json", "a")
        f.write(r.text)
        f.close()

        y = json.loads(r.text)

        if not y["result"]:
            print("result empty")
            return False

        self.message = y["result"][-1]['message']['text']
        self.chat_id = y["result"][-1]['message']['chat']['id']
        self._offset = y["result"][-1]["update_id"] + 1
        return True

    def sendMessage(self, text):
        ploads = {'chat_id':bot.chat_id, 'text':text}
        r = requests.get(bot_url + "sendMessage", params=ploads)
        if (r.status_code != 200):
            print(r.status_code)
            return False


bot = Bot()

cycle = True
while cycle == True:
    # cycle = False
    if not bot.getLastUpdate():
        time.sleep(1)
        continue
    reverse_message = bot.message[::-1]
    print(reverse_message)
    bot.sendMessage(reverse_message)
    time.sleep(1)
    # for elem in result["message"]:
    #     print(type(elem), elem)
