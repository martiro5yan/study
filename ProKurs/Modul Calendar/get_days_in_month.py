from datetime import *
import calendar

def get_days_in_month(year,month):
    month_name = list(calendar.month_name)
    del month_name[0]
    for i in month_name:
        if i == month:
            mnth = month_name.index(i) + 1
    max_day = calendar.monthrange(year,mnth)[1]
    start = date(year,mnth,1)
    end = date(year,mnth,max_day)
    list_day = []
    list_day.append(start)
    while start < end:
        start = start + timedelta(days=1)
        list_day.append(start)
    return list_day




print(get_days_in_month(1982, 'January'))