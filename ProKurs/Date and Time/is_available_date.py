from datetime import *
from colorama import init, Fore
from colorama import Back
from colorama import Style

from datetime import datetime

def converting_line_to_date(line):
    """Преобразование строки в объект datetime."""
    return datetime.strptime(line, '%d.%m.%Y')


def return_date_period(d):
    """Разделяет строку диапазона дат на две даты и возвращает их в виде списка объектов datetime."""
    dates = []
    for i in d.split('-'):
        dates.append(converting_line_to_date(i.strip()))
    return dates


def is_available_date(booked_dates, date_for_booking):
    """Проверяет доступность указанной даты или диапазона дат для бронирования."""
    list_blocked_dates = []
    desired_date = []

    # Преобразуем забронированные даты в объекты datetime
    for d in booked_dates:
        if '-' in d:
            list_blocked_dates.append(return_date_period(d))
        else:
            list_blocked_dates.append(converting_line_to_date(d))
    
    # Преобразуем даты для бронирования в объекты datetime
    if '-' in date_for_booking:
        desired_date = return_date_period(date_for_booking)
    else:
        desired_date.append(converting_line_to_date(date_for_booking))
    
    # Проверка пересечений
    if len(desired_date) == 1:  # Если бронируемая дата одна
        for d in list_blocked_dates:
            if isinstance(d, list):  # Забронированный период
                if desired_date[0] >= d[0] and desired_date[0] <= d[1]:
                    return False
            else:  # Забронированная одиночная дата
                if desired_date[0] == d:
                    return False
    else:  # Если бронируется период
        for d in list_blocked_dates:
            if isinstance(d, list):  # Забронированный период
                if desired_date[0] <= d[1] and desired_date[1] >= d[0]:
                    return False
            else:  # Забронированная одиночная дата
                if desired_date[0] <= d and desired_date[1] >= d:
                    return False

    # Если пересечений нет
    return True
    

print(Fore.GREEN +'TEST_1:')
print(Style.RESET_ALL)
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_2:')
print(Style.RESET_ALL)
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_3:')
print(Style.RESET_ALL)
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_4:')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_5:')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_6:')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '15.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_7:')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '17.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_8:')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_9:')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_10')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_11')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_12')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_13')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_14')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_15')
print(Style.RESET_ALL)
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_16')
print(Style.RESET_ALL)
dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_17')
print(Style.RESET_ALL)
dates = ['14.09.2022-14.10.2022']
some_date = '14.11.2022'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_18')
print(Style.RESET_ALL)
dates = ['14.09.2022-14.10.2022']
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_19')
print(Style.RESET_ALL)
dates = ['14.09.2022-14.10.2022']
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date))
print()
print(Fore.GREEN +'TEST_20')
print(Style.RESET_ALL)
dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '04.11.2021'
print(is_available_date(dates, some_date))
print()