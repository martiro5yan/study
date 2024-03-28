import sys

check_list = [] 
def processing(arr,category):
    for line in arr:
        news = line.split('/')
        if news[1].strip() == category:
            tpl = (news[0].strip(),float(news[2].strip('\n')))
            check_list.append(tpl)
    check_list.sort(key=lambda a: a[0])
    check_list.sort(key=lambda a: a[1])
    for i in check_list:
        print(i[0])
        

arr = []
for line in sys.stdin:
    arr.append(line.strip('\n'))
    if len(line) < 15:
        break

category = arr[-1]
arr.pop()
processing(arr,category)