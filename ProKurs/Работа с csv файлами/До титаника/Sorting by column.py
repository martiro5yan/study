import csv

n = int(input())
column_number = n - 1
ls = []
with open('deniro.csv', 'r', encoding='utf-8') as file:
    lists = csv.reader(file)
    for i in lists:
        ls.append(i)
    if column_number == 0:
        ls.sort(key=lambda i: i[column_number])
    else:
        ls.sort(key=lambda i: int(i[column_number]))
    for i in ls:
        print(i[0] + ',' + i[1] + ',' + i[2])
