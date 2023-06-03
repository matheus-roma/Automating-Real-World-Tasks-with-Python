import json, requests

url = 'https://www.google.com'
response = requests.get(url)

# if not response.ok:
#     raise Exception("GET failed with status code {}".format(response.status_code))

response.raise_for_status()


with open("people.json", "r") as people_json:
    people = json.load(people_json)

print(response.status_code)