#Функция должна возвращать список, элементами которого являются слова из списка words,
#которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм,
#функция должна вернуть пустой список.

def filter_anagrams(word,words):
    sort_word = sorted(word)
    word = ''.join(sort_word)
    anagram = []
    for i in words:
        sort_i = sorted(i)
        ii = ''.join(sort_i)
        if word == ii:
            anagram.append(i)
    return anagram



#filter_anagrams('tommarvoloriddle')
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('стекло', []))