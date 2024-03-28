from datetime import date

def print_good_dates(dates):
    sortList = []
    for d in dates:
        if d.strftime('%Y') == '1992' and (int(d.strftime('%m'))+ int(d.strftime('%d'))) == 29:
            sortList.append(d)
    sortList.sort()
    for d in sortList:
        print(d.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)