from datetime import *

def Converting_blocked(block): # заблокированные даты
    listBlocked = []
    gap = []
    for d in block:
        if len(d) == 10:
            listBlocked.append(datetime.strptime(d,'%d.%m.%Y').date())
        if len(d) == 21:
            line = d.split('-')
            for i in line:
                gap.append(datetime.strptime(i,'%d.%m.%Y').date())
    listBlocked.append(gap)
    return listBlocked
def Converting_desired_date(line): # желаемая дата
    if len(line) == 10:
        return datetime.strptime(line,'%d.%m.%Y').date()
    if len(line) == 21:
        line = line.split('-')
        start = datetime.strptime(line[0],'%d.%m.%Y').date()
        end = datetime.strptime(line[1],'%d.%m.%Y').date()
        return [start,end]
def is_available_date(booked_dates,date_for_booking):
    desired = Converting_desired_date(date_for_booking) # желаемый datetime
    blocked = Converting_blocked(booked_dates) # занятые datetime

    



dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))