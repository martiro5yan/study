# Day 55 / File operations
# На вход список названий файлов (lisntFile)
# Вывод файл output.txt с содержимым всех полученых файлов
def File_concatenation(listFile):
    output = []
    def Gluing(fileName):
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.readlines()
            for line in content:
                output.append(line)
    def newOutput(line):
        with open('output.txt','a', encoding='utf-8') as file:
            file.write(line)
    for fileName in listFile:
        Gluing(fileName)

    for line in output:
        newOutput(line)
    print('The file output.txt assembled!')
