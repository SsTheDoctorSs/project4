import requests
import os
from save_picture import save_picture
from pathlib import Path
from option import get_option
from dotenv import load_dotenv


def save_nasa_pictures(folder_name, api_key, count_of_links):
    website = 'https://api.nasa.gov/planetary/apod/'

    params = {"api_key": api_key, "count": count_of_links}
    response = requests.get(website, params=params)
    response.raise_for_status()
    get_nasa_image = response.json()
    for image in get_nasa_image:
        if image["url"] and image["media_type"] == 'image':
            images_link = image["url"]
            extention, filename = get_option(images_link)
            path = os.path.join(folder_name, f'{filename}{extention}')
            save_picture(images_link, path)


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    count_of_links = int(input())
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    save_nasa_pictures(folder_name, api_key, count_of_links)


if __name__ == '__main__':
    main()
