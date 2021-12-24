import yaml
import requests
import json

# Чтение конфигурации
with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Запрос данных API Home Assistant
url = config['url'] + "/api/states"
headers = {
    "Authorization": "Bearer " + config['token'],
}
response = requests.request("GET", url, headers=headers)

data = json.loads(response.content)   

# Получаем entity_id из группы
#print(response.text)
#print(data['entity_id']['person.vilensia'])
for item in data:
    if item["entity_id"] == config['group']:
        entity_ids = item["attributes"]['entity_id']
        print(entity_ids)
        # Поиск датчиков
        for entity_id in entity_ids:
            for entity in data:
                if entity["entity_id"] == entity_id:
                    print(entity["state"])
                    print(entity["attributes"])
