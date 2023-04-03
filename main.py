import telegram
import os
import random
import time

telegram_token = os.environ['TG_TOKEN']
chat_id = os.environ['TG_CHAT_ID']
time_test = os.environ['time_test']
period = os.environ['TIME']
bot = telegram.Bot(token=telegram_token)
dir_name = 'images'
filesindir = os.listdir(dir_name)
while True:
    random.shuffle(filesindir)
    for file in filesindir:
        bot.send_document(chat_id=chat_id, document=with open(f'{dir_name}/{file}', 'rb'))
        time.sleep(int(period))
