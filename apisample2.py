import requests
import json

url = 'https://catfact.ninja/fact'

response = requests.get(url)
print(response.json())

data ={"fact":"Cats are weird",'length':14}
response = requests.post(url, json = data)
print(response.json())