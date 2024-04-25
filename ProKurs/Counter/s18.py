
from collections import Counter

s = input().split(',')

result = Counter(s)
result = dict(sorted(result.items(),key=lambda x: x[0]))

lkey = []
for key in result:
    lkey.append(len(key))

mx = max(lkey)   
p = ' '
for k,v in result.items():
    n = mx - len(k)
    UC = 0
    for c in k:
        if c != ' ':
            UC += ord(c)
    print(f'{k}{p*n}: {UC} UC x {v} = {UC * v} UC')