import json

resuls = []

def if_str(line):
    line2 = line + '!'
    resuls.append(line2)

def if_number(number):
    resuls.append(number+1)

def if_bool(B):
    if B == True:
        B = False
        resuls.append(B)
    else:
        B=True
        resuls.append(B)

def if_list(l):
    resuls.append(l+l)

def if_dict(data):
    data["newkey"] = None
    resuls.append(data)

dictionary_of_functions = {str :if_str, int :if_number, bool :if_bool, list :if_list, dict :if_dict}

with open('data.json','r',encoding='UTF-8') as file:
    data_json = json.loads(file.read())

    for i in data_json:
        if type(i) in dictionary_of_functions:
            dictionary_of_functions[type(i)](i)

with open('updated_data.json','w',encoding='UTF-8') as file:
    list_jsone = json.dumps(resuls)
    json.dump(resuls,file)

