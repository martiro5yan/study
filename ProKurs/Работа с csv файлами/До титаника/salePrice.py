import csv

with open('sales.csv', 'r', encoding='utf-8') as file_csv:
    file = csv.reader(file_csv, delimiter=';', quotechar='"')
    next(file)
    for line in file:
        if int(line[1]) > int(line[2]):
            print(line[0])