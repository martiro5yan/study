from datetime import *
import sys


def converting_line_to_date(line):
    """Преобразование строки в объект datetime."""
    return datetime.strptime(line, '%d.%m.%Y').date()

def asc_test(dates):
    for i in range(len(dates)-1):
        if dates[i] >= dates[i+1]:
            return False
    return True
    

def desc_test(dates):
    for i in range(len(dates)-1):
        if dates[i] <= dates[i+1]:
            return False
    return True

dates = []

for line in sys.stdin:
    d = line.strip('\n')
    dates.append(converting_line_to_date(d))

if asc_test(dates):
    print('ASC')
elif desc_test(dates):
    print('DESC')
else:
    print('MIX')
