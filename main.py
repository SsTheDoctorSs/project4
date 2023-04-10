import telegram
import os
import random
import time
from pathlib import Path
from telegram.error import NetworkError

def main():
    telegram_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    time_test = os.environ['time_test']
    period = os.environ['TIME']
    bot = telegram.Bot(token=telegram_token)
    dir_name = 'images'
    filesindir = os.listdir(dir_name)
    while True:
        try:
        random.shuffle(filesindir)
        for file in filesindir:
            path_file = os.path.join(dir_name, file)
            with open(path_file, 'rb') as doc:
                bot.send_document(chat_id=chat_id, document=doc)
            time.sleep(int(period))
       except NetworkError:
            print('Ошибка сети')
if __name__ == '__main__':
    main()
