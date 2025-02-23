import requests
import json

cso_data = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(cso_data)
data = response.json()

with open("cso.json", "w") as file:
    json.dump(data, file)