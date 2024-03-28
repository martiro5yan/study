import calendar


s = input().split()
year = int(s[0])
month_name = list(calendar.month_name)
del month_name[0]
for i in month_name:
    if i == s[1]:
        ind = month_name.index(i) + 1

print(calendar.monthrange(year,ind)[1])
