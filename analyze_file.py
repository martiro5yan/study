#Day 53
# Выводит кольво строк, слов и символов
def analyze_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        content = file.read()
        quantity_words = len(content.split())  # Количество слов
        quantity_letters = sum(c.isalpha() for c in content)  # Количество букв
        quantity_lines = content.count('\n') + 1  # Количество строк
        print(f'Analysis of {file_name}:')
        print(f'{quantity_letters} letters')
        print(f'{quantity_words} words')
        print(f'{quantity_lines} lines')

file_name = input()
analyze_file(file_name)