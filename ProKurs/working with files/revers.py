import sys

def reverse(line):
    return line[::-1]

for line in sys.stdin:
    print(reverse(line.strip('\n')))
    