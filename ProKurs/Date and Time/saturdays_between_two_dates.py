from datetime import date,timedelta

def listday(end,start):
    listdate = []
    current_date = end
    while current_date <= start:
        listdate.append(current_date)
        current_date += timedelta(days=1)
    return listdate

def saturdays_between_two_dates(start,end):
    listdate = []
    if start > end:
        count = 0
        for i in listday(end,start):
            if i.weekday() == 5:
                count += 1
        return count

    current_date = start
    while current_date <= end:
        listdate.append(current_date)
        current_date += timedelta(days=1)
    count = 0
    for i in listdate:
        if i.weekday() == 5:
            count += 1
    return count
    