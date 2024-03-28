import calendar

s = input().split()


abbr_name = list(calendar.month_abbr)
del abbr_name[0]

for i in abbr_name:
    if i == s[1]:
        ind = abbr_name.index(s[1])
m = ind + 1
print(calendar.month(int(s[0]),m))