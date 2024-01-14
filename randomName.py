# Day 53
# Random name and surname

from random import *

with open('first_names.txt') as file:
    content = file.readlines()
    first_names = []
    for line in content:
        first_names.append(line.rstrip())
    first_list = []
    for i in range(1,4):
        idx = randint(1,len(first_names)-1)
        first_list.append(first_names[idx])
    #print(first_list)
with open('last_names.txt') as file:
    content = file.readlines()
    last_names = []
    for line in content:
        last_names.append(line.rstrip())
    last_list = []
    for i in range(1,4):
        idx = randint(1,len(last_names)-1)
        last_list.append(last_names[idx])
    #print(last_list)
for i in range(0,3):
    print(first_list[i],last_list[i])