import requests
import os
from pathlib import Path
from datetime import datetime
from save_picture import save_picture
from dotenv import load_dotenv


def save_EPIC_pictures(folder_name, api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    EPIC_images = response.json()
    for image in EPIC_images:
        images_link = image["image"]
        image_date = image["date"]
        date = datetime.fromisoformat(image_date).strftime('%Y/%m/%d')
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{images_link}.png'
        path = os.path.join(folder_name, f'{images_link}.png')
        save_picture(link, path, params)


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    save_EPIC_pictures(folder_name, api_key)


if __name__ == '__main__':
    main()
