import csv

with open('salary_data.csv', 'r', encoding='utf-8') as csv_file:
    file = csv.reader(csv_file, delimiter=';')
    list_file = list(file)
    del list_file[0]

    list_dicts = {}
    for line in list_file:
        key = line[0]
        value = line[1]
        if key not in list_dicts:
            list_dicts[key] = [] 
        list_dicts[key].append(value)
    
    result_list = []

    for key, value in list_dicts.items():
        sum_vl = sum(map(int, value))
        ln_vl = len(value)
        res = sum_vl / ln_vl
        result_list.append([key, res])
    
    result_list.sort(key=lambda i: (i[1], i[0]))  # Сначала сортируем по средней зарплате, затем по названию компании
    
    for i in result_list:
        print(i[0], '______', i[1])