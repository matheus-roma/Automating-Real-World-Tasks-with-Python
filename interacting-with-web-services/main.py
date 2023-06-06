import json, requests, os

cwd = os.getcwd()
feedbackDir = f"{cwd}/data/feedback"
corpweb_external_IP = "35.222.178.179"

data = []
for filename in os.listdir(feedbackDir):
    file_path = os.path.join(feedbackDir, filename)
    if file_path.endswith(".txt"):
        with open(file_path, "r") as file:
            data.append({"title" : file.readline().strip("\n"),
                              "name" : file.readline().strip("\n"),
                              "date" : file.readline().strip("\n"),
                              "feedback" : file.readline().strip("\n")})

# with open("feedbacks.json", "w") as feedbacks_json:
#     json.dump(data, feedbacks_json, indent=2)

for item in data:
    web_feedback = requests.post(f"http://{corpweb_external_IP}/feedback/", data=item)
    web_feedback.raise_for_status()

print("ok")