from collections import Counter

with open('pythonzen.txt','r', encoding='UTF-8') as file:
    s = file.readlines()
    arr = []
    for i in s:
        arr.append(i.lower())
    line = ''.join(arr)
    
    result = Counter(line)
    result = dict(sorted(result.items(), key=lambda x: x[0]))
    
    for k,v in result.items():
        if k.isalpha():
            print(f'{k}: {v}')