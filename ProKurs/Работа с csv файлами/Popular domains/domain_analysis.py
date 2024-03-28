import csv

domain_count = {}
def count_domain(domain): # подсчет количества встречающихся доменов
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1
     
domain_list = []
def extract_domain(email): # Извлечение домена из адреса электронной почты
    domain = email.split('@')[1]
    domain_list.append(domain)
    count_domain(domain)

with open('filename','r',encoding='utf-8') as csvfile: # Открытие файла для чтения
    file = csv.reader(csvfile)
    next(file)  # Пропуск заголовка
    for row in file:
        extract_domain(row[2])

sorted_domains = sorted(domain_count.items(), key=lambda x: (x[1], x[0])) # Сортировка доменов по количеству встречаемости и алфавиту
header = ['domain', 'count']

with open('newfilename.csv', 'w', encoding='utf-8', newline='') as file: # Открытие файла для записи результата
    csv_writer = csv.DictWriter(file, fieldnames=header)
    csv_writer.writeheader()                
    for domain, count in sorted_domains:
        csv_writer.writerow({'domain': domain, 'count': count})
