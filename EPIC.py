import requests
import os
from pathlib import Path
from datetime import datetime
from save_picture import save_picture
from dotenv import load_dotenv

def save_EPIC_pictures(folder_name):
    website = 'https://api.nasa.gov/EPIC/api/natural/images'
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key}
    response = requests.get(website, params=params)
    response.raise_for_status()
    get_EPIC_image = response.json()
    for image in get_EPIC_image:
        images_link = image["image"]
        image_date = image["date"]
        date = datetime.fromisoformat(image_date).strftime('%Y/%m/%d')
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{images_link}.png'
        path = os.path.join(folder_name, f'{images_link}.png')
        save_picture(link, path, params)
def main():
    load_dotenv()
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    save_EPIC_pictures(folder_name)
if __name__ == '__main__':
    main()
