class TextHandler:
    def __init__(self):
        self.arr = []

    # Сбор слов
    def add_words(self, line):
        line = line.split()
        self.arr.extend(line)
        self.mn = len(min(self.arr,key=len))
        self.mx = len(max(self.arr,key=len))

    # Самые короткие слова
    def get_shortest_words(self):
        shortest_words = []
        for word in self.arr:
            if len(word) == self.mn:
                shortest_words.append(word)
        return shortest_words

    # Самые длинные слова    
    def get_longest_words(self):
        longest_word = []
        for word in self.arr:
            if len(word) == self.mx:
                longest_word.append(word)
        return longest_word


texthandler = TextHandler()
texthandler_1 = TextHandler()

texthandler_1.add_words('''Я помню чудное мгновенье
Передо мной явилась ты
Как мимолетное виденье
Как гений чистой красоты

В томленьях грусти безнадежной
В тревогах шумной суеты
Звучал мне долго голос нежный
И снились милые черты

Шли годы Бурь порыв мятежный
Рассеял прежние мечты
И я забыл твой голос нежный
Твои небесные черты

В глуши во мраке заточенья
Тянулись тихо дни мои
Без божества без вдохновенья
Без слез без жизни без любви

Душе настало пробужденье
И вот опять явилась ты
Как мимолетное виденье
Как гений чистой красоты

И сердце бьется в упоенье
И для него воскресли вновь
И божество и вдохновенье
И жизнь и слезы и любовь''')

texthandler_1.mn = 5

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')
 
print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
print()
print(texthandler_1.get_longest_words())
print(texthandler_1.get_shortest_words())