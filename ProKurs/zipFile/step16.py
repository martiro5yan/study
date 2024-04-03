from zipfile import ZipFile

result = []

def calculations(Vc,Vo,name):
    K = (Vc / Vo) * 100
    result.append((name,K))

with ZipFile('workbook.zip', mode='r') as zFile:
    info = zFile.infolist()

    for i in range(len(info)):
        if info[i].is_dir():
            directory_name = info[i].filename
           
            for file_info in zFile.infolist():
                if file_info.filename.startswith(directory_name):
                    if file_info.file_size > 0:
                        name = file_info.filename.split('/')
                        calculations(file_info.compress_size,file_info.file_size,name[1])
        elif info[i].is_dir() == False:
            if '/' in info[i].filename:
                name = info[i].filename.split('/')
                #print(name[1])
                calculations(info[i].compress_size,info[i].file_size,name[1])

r = min(result, key=lambda x: x[1])

print(r[0])