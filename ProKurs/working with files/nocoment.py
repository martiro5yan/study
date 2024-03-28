import sys
#не работает !
for line in sys.stdin:
    line = line.strip()
    if line == '\n':
        continue
    if line[0] != '#':
        print(line.strip('\n'))  



