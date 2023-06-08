#!/usr/bin/env python3
import os, json, requests

descriptions_path = "supplier-data/descriptions"
images_path = "supplier-data/images"
url = "http://localhost/fruits/"

data = []
for filename in os.listdir(descriptions_path):
    f = os.path.join(descriptions_path, filename)
    img = os.path.join(images_path, filename)
    # checking if it is a file
    if f.endswith(".txt"):
        with open(f, "r") as file:
            data.append({"name" : file.readline().strip("\n"),
            "weight" : int(file.readline().strip("\n").rstrip(" lbs")),
            "description" : file.readline().strip("\n"),
            "image_name" : f"{filename.rstrip('.txt')}.jpeg"})

with open("feedbacks.json", "w") as feedbacks_json:
    json.dump(data, feedbacks_json, indent=2)


for item in data:
    print(item)
    post_fruits = requests.post(url, data=item)
    post_fruits.raise_for_status()