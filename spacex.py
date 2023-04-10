import requests
import os
from pathlib import Path
from save_picture import save_picture


def save_spacex_pictures(folder_name):
    website = 'https://api.spacexdata.com/v3/launches/'
    response = requests.get(website)
    response.raise_for_status()
    get_spacex_image = response.json()
    for link in get_spacex_image:
        images_link = link["links"]["flickr_images"]
        if link["links"]["flickr_images"]:
            break

    for link_number, link in enumerate(images_link):
        filename = f'spacex{link_number}.jpg'
        path = os.path.join(folder_name, filename)
        save_picture(link, path)


def main():
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    save_spacex_pictures(folder_name)


if __name__ == '__main__':
    main()
