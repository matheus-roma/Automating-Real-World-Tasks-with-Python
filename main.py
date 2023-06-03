import json, requests, os

resourcesDir = "resources"

data = {}
for filename in os.listdir(resourcesDir):
    file_path = os.path.join(resourcesDir, filename)
    if file_path.endswith(".txt"):
        with open(file_path, "r") as file:
            data[filename] = {"title" : file.readline().strip("\n"),
                              "name" : file.readline().strip("\n"),
                              "date" : file.readline().strip("\n"),
                              "feedback" : file.readline().strip("\n")}

#with open("feedbacks.json", "w") as feedbacks_json:
#    json.dump(data, feedbacks_json, indent=2)

#print(data)


            
