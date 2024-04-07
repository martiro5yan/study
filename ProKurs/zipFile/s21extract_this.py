from zipfile import ZipFile

def extract_this(zip_name,*args):
    if len(args) == 0:
        with ZipFile(zip_name) as zip_file:
            zip_file.extractall()
    else:
        with ZipFile(zip_name) as zip_file:
            info = zip_file.infolist()
            
            for i in range(len(info)):
                if info[i].is_dir() == True:
                    directory_name = info[i].filename
                    for file_info in zip_file.infolist():
                        if file_info.filename.startswith(directory_name):
                            n = zip_name.split('.')
                            road = f'{n[0]}/{file_info.filename}'
                            s = road.split('/')
                            #print(road)
                            for i in args:
                                if i == s[2]:
                                    zip_file.extract(file_info.filename)

                else:
                    for filename in args:
                        if info[i].filename == filename:
                            zip_file.extract(filename)
            

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')