import sys

def revers(numbers):
    def rec(index):
        if index <= (len(numbers)-1):
            print(numbers[index])
            rec(index + 1)
    rec(0)
        
numbers = []

for n in sys.stdin:
    number = n.strip('\n')
    numbers.insert(0,int(number))
    if int(number) == 0:
        break

revers(numbers)