import telegram
import os
import random
import time
from pathlib import Path
from telegram.error import NetworkError


def main():
    telegram_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    period = int(os.environ.get('TIME', 14400))
    bot = telegram.Bot(token=telegram_token)
    dir_name = 'images'
    filesindir = os.listdir(dir_name)
    while True:
        random.shuffle(filesindir)
        try:
            for file in filesindir:
                path_file = os.path.join(dir_name, file)
                with open(path_file, 'rb') as doc:
                    bot.send_document(chat_id=chat_id, document=doc)
                time.sleep(int(period))
        except NetworkError:
            print('Ошибка сети')
            time.sleep(20)


if __name__ == '__main__':
    main()
