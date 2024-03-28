import json

with open('countries.json', 'r', encoding='UTF-8') as file:
    list_json = json.loads(file.read())

    religion_dict = {}
    
    for Dictionary in list_json:
        for key,value in Dictionary.items():
            if key == "religion" and value not in religion_dict:
                religion_dict[value] = []

    for d in list_json:
        for key, value in religion_dict.items():
            if d["religion"] == key:
                if d["country"] not in religion_dict[key]:
                    religion_dict[key].append(d["country"])

    with open('religion.json', 'w', encoding='UTF-8') as file:
        json.dump(religion_dict,file)
