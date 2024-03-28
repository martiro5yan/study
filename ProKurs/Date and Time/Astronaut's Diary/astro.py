from datetime import *
from collections import OrderedDict
with open('diary.txt', 'r') as file:
    content = file.read()
    content = content.split('\n\n')
    timeList = []
    textList = []
    for i in content:
        timeList.append(datetime.strptime([i][0][:17],'%d.%m.%Y; %H:%M')) # Создаем список для ключей
        textList.append([i][0][17:]) # Создаем список для значений

    astro_dict = dict(zip(timeList,textList)) # Создаем словарь
    sorted_dict = OrderedDict(sorted(astro_dict.items())) # Сортируем словарь по ключам с привязкой значений

    with open('diary.txt', 'w+') as file: # Перезаписываем файл с отсортированной датой 
        def new_astro(keytime,value):
            file.write(keytime)
            file.write(value + '\n\n')  
        for key in sorted_dict:
            keytime = key.strftime("%d.%m.%Y; %H:%M")
            new_astro(keytime,sorted_dict[key])
with open('diary.txt', 'r') as file:
        content = file.read()
        print(content)
        
        