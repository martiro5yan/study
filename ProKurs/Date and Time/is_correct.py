from datetime import date

def is_correct(day, month, year):
    try:
        if 1 <= day <=31 and 1 <= month <= 12:
            d = date(year, month, day)
            return 'Корректная'
        else:
            return 'Некорректная'
    except:
        return 'Некорректная'

count = 0
while True:
    s = input()
    if s == 'end':
        break
    else:
        d = s.split('.')
        day = int(d[0])
        month = int(d[1])
        year = int(d[2])
        res = is_correct(day,month,year)
        print(res)
        if res == 'Корректная':
            count += 1
print(count)