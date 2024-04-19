from collections import namedtuple
from datetime import datetime


with open('meetings.csv','r', encoding='UTF-8') as file:
    Friends = file.readlines()
    Person = namedtuple('Person', Friends[0])

    del Friends[0]
    result = []
    for i in Friends:
        p = i.strip('\n').split(',')
        person = Person._make(p)
        date_obj = datetime.strptime(person.meeting_date, "%d.%m.%Y")
        time_obj = datetime.strptime(person.meeting_time, "%H:%M").time()
        person = person._replace(meeting_date=date_obj, meeting_time=time_obj)
        result.append(person)
    
    sort_result = sorted(result,key=lambda x: (x[2],x[3]))

    for i in sort_result:

        print(i.surname,i.name)