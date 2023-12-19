#Day 41

# Перевод строки в словарь
# Формат ввода " 1:test line:line ... "
def translating_line_into_a_dictionary(line):
    line = line.split(' ')
    key = []
    val = []
    for i in line:
        i = i.split(':')
        key.append(i[0])
        val.append(i[1])
        result = dict(zip(key,val))
    return result