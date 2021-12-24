import yaml
import requests
import json

# Чтение конфигурации
with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Запрос данных API Home Assistant
def states_ha
url = config['url'] + "/api/states/group.ha_kodi"
headers = {
    "Authorization": "Bearer " + config['token'],
}
response = requests.request("GET", url, headers=headers)

data = json.loads(response.content)   

# Получаем entity_id из группы
print(data['attributes']['entity_id'])
