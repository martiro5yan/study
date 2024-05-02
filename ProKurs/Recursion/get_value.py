# def get_value(nested_dicts,key):
#     if key in nested_dicts:
#         return nested_dicts[key]
    
#     for v in nested_dicts.values():
#         if type(v) == dict:
#             value = get_value(v, key)    # рекурсивный случай
#             if value is not None:
#                 return value 




# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

# print(get_value(data, 'cityName'))

arr = set()
def get_all_values(nested_dicts,key):
    if key in nested_dicts:
        arr.add(nested_dicts[key])
    if type(nested_dicts) == dict:
        for v in nested_dicts.values():
            if type(v) == dict:
                get_all_values(v, key)        
    return arr



my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
print(type(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))