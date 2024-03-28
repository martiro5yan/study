from datetime import date, timedelta

def get_date_range(start,end):
    listdate = []

    if start > end:
        return listdate
    elif start == end:
        listdate.append(start)
        return listdate
    
    current_date = start
    while current_date <= end:
        listdate.append(current_date)
        current_date += timedelta(days=1)
    return listdate
date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')