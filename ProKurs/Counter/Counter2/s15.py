from collections import defaultdict

words = input().lower().split()

list_word = defaultdict(list)
for word in words:
    list_word[len(word)].append(word)

for k,v in sorted(list_word.items(), key=lambda x: len(x[1])):
    print(f'Слов длины {k}: {len(v)}')