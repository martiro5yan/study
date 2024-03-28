import json


def is_correct_json(line):
    try:
        json_line = json.loads(line)
        return True
    except ValueError:
        return False



data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))

#print(is_correct_json('number = 17'))