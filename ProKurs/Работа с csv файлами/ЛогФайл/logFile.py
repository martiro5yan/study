import csv

with open('name_log.csv', 'r', encoding='UTF-8') as file:
    arr = csv.reader(file)
    arr = list(arr)
    header = arr.pop(0)
    for i in arr:
        print(i)