import sys
arr = []
for line in sys.stdin:
    arr.append(int(line.strip('\n')))

if len(arr) == 0:
    print('нет учеников')
else:
    mx = max(arr)
    mn = min(arr)
    sr = sum(arr) / len(arr)   
    print(f'Рост самого низкого ученика: {mn}')
    print(f'Рост самого высокого ученика: {mx}')
    print(f'Средний рост: {sr}')