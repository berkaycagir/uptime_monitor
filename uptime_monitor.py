#!/usr/bin/python3

BOT_TOKEN = "TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = "CHAT_ID_WITH_BOT_HERE"
# You can add additional check targets to the list below.
TARGETS = ["https://www.google.com", "https://github.com"]

import requests

def telegram_bot_sendtext(bot_token, bot_chatID, bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

if __name__ == "__main__":
    for url in TARGETS:
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            telegram_bot_sendtext(BOT_TOKEN, CHAT_ID, "Warning! Exception raised when trying to check " + url + ", you should take a look.")
        if not r.ok or r.status_code != 200:
            telegram_bot_sendtext(BOT_TOKEN, CHAT_ID, "Warning! Status code from request to " + url + " is not 200, you should take a look.")