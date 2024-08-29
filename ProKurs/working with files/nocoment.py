import sys

for line in sys.stdin:
    line = line.strip()
    if line == '\n':
        print()

    if line[0] != '#':
        print(line.strip('\n'))  



