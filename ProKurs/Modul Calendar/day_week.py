from datetime import *
import calendar

dat = datetime.strptime(input(),'%Y-%m-%d').date()
n = datetime.weekday(dat)
print(calendar.day_name[n])