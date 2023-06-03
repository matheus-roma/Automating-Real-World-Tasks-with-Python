import json, requests, os

resourcesDir = "resources"

data = {}
for filename in os.listdir(resourcesDir):
    file_path = os.path.join(resourcesDir, filename)
    if file_path.endswith(".txt"):
        with open(file_path, "r") as file:
            data[filename] = file.read()

print(data)


            
