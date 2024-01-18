# Day 54
with open('input.txt', 'r') as file:
    contentFile = file.readlines()
    content = []
    for i in contentFile:       #Удаление переноса строки и перезапись в список
        line = i.rstrip()
        content.append(line)
    res = []
    for i in content:           #Нумерация строк
        num = content.index(i)+1
        line = (str(num)+') ')+i
        res.append(line)

def writing_to_a_file(line): # Cоздание нового файла с пронумерованными строками
    with open('output.txt', 'a', encoding='utf-8') as file:
        file.write(str(line) + '\n')

for i in res:           #Запись строк 
    writing_to_a_file(i)