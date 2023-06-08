#!/usr/bin/env python3
import os
from PIL import Image

image_path = "supplier-data/images"
size = (600,400)

for filename in os.listdir(image_path):
    f = os.path.join(image_path, filename)
    # checking if it is a file
    try:
        with Image.open(f).convert("RGB") as im:
            im.thumbnail(size)
            filename = filename.rstrip(".tiff")
            print(f"{image_path}/{filename}.jpeg")
            #im.save(f"{image_path}/{filename}.jpeg")
    except IOError:
        pass