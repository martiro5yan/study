from collections import Counter

def count_occurences(word,words):
    words = Counter(words.lower().split())
    return words[word.lower()]
#TEST 1
word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))