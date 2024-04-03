from zipfile import ZipFile
import datetime

result = {}

with ZipFile('workbook.zip', mode='r') as zFile:
    info = zFile.infolist()

    for i in range(len(info)):
        if info[i].is_dir() == True:
            directory_name = info[i].filename
           
            for file_info in zFile.infolist():
                if file_info.filename.startswith(directory_name):
                    if file_info.file_size > 0:
                        name = file_info.filename.split('/')
                        result[name[1]] = [file_info.date_time,
                                           file_info.file_size,
                                           file_info.compress_size]
                                            
        else:
            if '/' in info[i].filename:
                #print(info[i].date_time,name[1])
                name = info[i].filename.split('/')
                #print(name[1])
                result[name[1]] = [info[i].date_time,
                                   info[i].file_size,
                                   info[i].compress_size]
            else:
                result[info[i].filename] = [info[i].date_time,
                                            info[i].file_size,
                                            info[i].compress_size]

r = dict(sorted(result.items()))

for key,value in r.items():
    d = datetime.datetime(*value[0])
    print(key)
    print(f'  Дата модификации файла: {d}')
    print(f'  Объем исходного файла: {value[1]} байт(а)')
    print(f'  Объем сжатого файла: {value[2]} байт(а)')
    print()