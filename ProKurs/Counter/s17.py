from collections import Counter

s = input().split(',')

result = Counter(s)
result = dict(sorted(result.items(),key=lambda x: x[0]))

for k,v in result.items():
    print(f'{k}: {v}')
