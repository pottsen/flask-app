import requests
import json

# url = 'http://127.0.0.1:5000/helloname'  # localhost and the defined port + endpoint
# body = {
#     "name": "Peter"
# }
# response = requests.post(url, data=body)
# print(response.json())

url = 'http://127.0.0.1:5000/countries'  # localhost and the defined port + endpoint
body = {
    "id": 1,
    "name": "Murica",
    "capital": "Freedon", 
    "area": 1000000
}
response = requests.post(url, data=body)
print(response.json())

