
# step13
# from collections import Counter

# line = input().lower().split()

# counter = Counter(line)
# result = []
# result = sorted(counter.items(), key=lambda x: x[1])
# print(result[::-1][0][0])


from collections import Counter

line = input().lower().split()

counter = Counter(line)

#mn = counter.most_common()[::-1][0][1]
mx = counter.most_common()[0][1]

resutl = []
for i in counter.most_common()[::-1]:
    if i[1] == mx:
        
        resutl.append(i[0])

r = max(sorted(resutl))
#r = ', '.join(r)
print(r)