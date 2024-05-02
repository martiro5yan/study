from datetime import *

def date_formatter(counrty_code):
    def forrmat_change(date):
        d = {'ru': '%d.%m.%Y',
            'us': '%m-%d-%Y',
            'ca': '%Y-%m-%d',
            'br': '%d/%m/%Y',
            'fr': '%d.%m.%Y',
            'pt': '%d-%m-%Y',}
        if counrty_code in d:
            result = datetime.strftime(date,d[counrty_code])
            return result
        
    return forrmat_change

date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))