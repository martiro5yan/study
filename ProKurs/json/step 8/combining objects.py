import json

with open('data1.json', 'r', encoding='UTF-8') as file_1, open('data2.json', 'r', encoding='UTF-8') as file_2:
    data1_json = json.load(file_1)
    data2_json = json.load(file_2)

# Объединение JSON-объектов, предпочтение отдается значениям из второго объекта
merged_data = {**data1_json, **data2_json}

with open('data_merge.json', 'w', encoding='UTF-8') as file:
    json.dump(merged_data, file)
