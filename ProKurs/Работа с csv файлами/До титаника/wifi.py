import csv

#Cоздание словаря
count_access = {}
def count_access_point(address):
    if address[0] in count_access:
        count_access[address[0]] += address[1]
    else:
        count_access[address[0]] = address[1]

#Извлечение района и количества точек доступа
def extract_district_and_access_points(district,access_points):
    address = [district,access_points]
    count_access_point(address)

#Открытие файла 
with open('wifi.csv', 'r', encoding='utf-8') as file:
    file_csv = csv.reader(file, delimiter=';')
    next(file_csv)
    for i in file_csv:
        extract_district_and_access_points(i[1],int(i[-1]))
#Cортировка
sort_distict = sorted(count_access.items(), key=lambda x: (-x[1], x[0]))
#Вывод
for tuple in sort_distict:
    print(f'{tuple[0]}: {tuple[1]}')
