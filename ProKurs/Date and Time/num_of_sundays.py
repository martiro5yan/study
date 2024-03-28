from datetime import *

def num_of_sundays(year):
    first_d = date(year,1,1)
    last_d = date(year,12,31)
    c_day = first_d
    count = 0
    while c_day<=last_d:
        if c_day.weekday() == 6:
            count +=1
        c_day += timedelta(days=1)
    return count



print(num_of_sundays(2021))