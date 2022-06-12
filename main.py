import requests
import json
import pprint

baseurl = 'https://api.openweathermap.org/data/2.5/onecall'
lat = '29.3867'
lon = '73.9031'
API_KEY = '456030954b1d645fb1bc07f48ae31b44'
exclude = "hourly,daily"

url1 = baseurl + '?lat=' + lat + '&lon=' + lon + "&exclude=" + exclude + '&appid=' + API_KEY
print(url1)

response = requests.get(url1)
pprint.pprint(response.json())


