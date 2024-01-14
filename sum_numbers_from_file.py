#Day 47
#Сумма чисел в строках
def sum_numbers_in_file(filename):
    with open(filename, encoding='utf-8') as file:
        content = file.readlines()
        for i in content:
            lines = i.split()
            result = list(map(int, lines))
            print(sum(result))

filename = input()

sum_numbers_in_file(filename)
sum_numbers_from_file.py
