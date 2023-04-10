import os
from urllib.parse import urlparse, unquote


def get_option(link):
    cut_link = unquote(link)
    divided_link = urlparse(cut_link)
    path, filename = os.path.split(divided_link.path)
    file_extension = os.path.splitext(filename)
    filename, extension = file_extension
    return extension, filename
