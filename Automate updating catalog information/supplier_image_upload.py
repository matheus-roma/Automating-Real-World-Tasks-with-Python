#!/usr/bin/env python3
import requests, os, mimetypes
from PIL import Image

# This example shows how a file can be uploaded using
# The Python Requests module

image_path = "supplier-data/images"
url = "http://localhost/upload/"

for filename in os.listdir(image_path):
    f = os.path.join(image_path, filename)
    # checking if it is a file
    try:
        if opened.name.endswith(".jpeg"):
            with open(f, 'rb') as opened:
                r = requests.post(url, files={'file': opened})    
    except IOError:
        pass
    

