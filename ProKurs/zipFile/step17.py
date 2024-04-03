from zipfile import ZipFile
import datetime

result = []

def favorites(d,name):
    deadline = datetime.datetime(2021,11,30,14,22,00)
    after = datetime.datetime(*d)
    if deadline < after:
        if name not in result:
            result.append(name)

with ZipFile('workbook.zip', mode='r') as zFile:
    info = zFile.infolist()

    for i in range(len(info)):
        if info[i].is_dir() == True:
            directory_name = info[i].filename
           
            for file_info in zFile.infolist():
                if file_info.filename.startswith(directory_name):
                    if file_info.file_size > 0:
                        name = file_info.filename.split('/')
                        favorites(file_info.date_time,name[1])
                            
        else:
            if '/' in info[i].filename:
                #print(info[i].date_time,name[1])
                name = info[i].filename.split('/')
                #print(name[1])
                favorites(info[i].date_time,name[1])
            else:
                favorites(info[i].date_time,info[i].filename)
                    
r = sorted(result)
#print(*r,sep='\n')