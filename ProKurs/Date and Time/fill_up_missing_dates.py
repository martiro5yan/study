from datetime import *

def fill_up_missing_dates(dates):
    date_list = []
    for date in dates:
        date_list.append(datetime.strptime(date,'%d.%m.%Y'))
    
    mn_date = min(date_list)
    mx_date = max(date_list)

    list_dates = []
    list_dates.append(mn_date)

    while mn_date < mx_date:
        mn_date = mn_date + timedelta(days=1)
        list_dates.append(mn_date)

    result = []
    for d in list_dates:
        result.append(d.strftime('%d.%m.%Y'))
    return result

dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
fill_up_missing_dates(dates)
