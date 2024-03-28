
import sys

def chek(string):
    test = 0
    for i in string:
        if i == ' ':
            test += 1
    
    if len(string) == test:
        return True
    else:
        False

count = 0
for line in sys.stdin:
    for string in line.strip('\n').split('#'):
        if len(string) == 0:
            count += 1
        if len(string) > 0:
            if chek(string):
                count += 1
            
print(count)