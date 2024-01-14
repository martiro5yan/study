with open('numbers.txt', encoding='utf-8') as file:
    content = file.readlines()
    for i in content:
        lines = i.split()
        result = list(map(int, lines))
        print(sum(result))
