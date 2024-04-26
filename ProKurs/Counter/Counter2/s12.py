from collections import Counter

line = input().lower().split()

counter = Counter(line)
print(counter.most_common())
print(counter.most_common()[0][0])