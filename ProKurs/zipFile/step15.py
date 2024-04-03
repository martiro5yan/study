from zipfile import ZipFile

with ZipFile('workbook.zip', mode='r') as zFile:
    info = zFile.infolist()
    compressed_file = 0
    the_source_file = 0
    
    for file in range(len(info)):
        the_source_file += info[file].file_size
        compressed_file += info[file].compress_size

print(f'Объем исходных файлов: {the_source_file} байт(а)')
print(f'Объем сжатых файлов: {compressed_file} байт(а)')