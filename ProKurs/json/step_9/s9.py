import json

with open('people.json','r', encoding='UTF-8') as file:
    json_list = json.loads(file.read())

    
    list_key = []

    for dictionary in json_list:
        for key in dictionary.keys():  # Перебираем ключи каждого словаря
            if key not in list_key:
                list_key.append(key)  # Добавляем новые ключи в list_key

    for dictionary in json_list:
        for key in list_key:
            if key not in dictionary:
                dictionary[key] = None

with open('updated_people.json', 'w', encoding='UTF-8') as file:
    json.dump(json_list,file)