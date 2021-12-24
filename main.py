import yaml
import requests

# Чтение конфигурации
with open('config.yaml') as f:
    config = yaml.safe_load(f)

url = config['url'] + "/api/states/sensor.basement_temperature"
headers = {
    "Authorization": "Bearer " + config['token'],
}
response = requests.request("GET", url, headers=headers)

print(response.text)
