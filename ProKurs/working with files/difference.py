import sys
from datetime import *

def difference(date_list):
    result = max(date_list)-min(date_list)
    return result.days

date_list = []
def transformation(line):
    date_list.append(datetime.strptime(line,'%Y-%m-%d'))
    
for line in sys.stdin:
    if line == '\n' or line =='':
        break
    else:
        transformation(line.strip('\n'))

print(difference(date_list))