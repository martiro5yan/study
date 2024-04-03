from zipfile import ZipFile

with ZipFile('workbook.zip', mode='r') as zFile:
    info = zFile.infolist()
    count = 0
    for i in range(len(info)):
        if info[i].is_dir() == False:
            count += 1

print(count)