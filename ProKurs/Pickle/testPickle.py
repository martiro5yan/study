import sys
import pickle


def deser(filename):
    l = []
    with open(filename,'rb') as file:
        obj = pickle.load(file)
        for s in sys.stdin:
            line = s.strip('\n')
            l.append(line)
    print(obj(*l))

filename = input()
deser(filename)