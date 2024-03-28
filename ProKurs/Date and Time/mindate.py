from datetime import date
listDate = []
for _ in range(2):
    listDate.append(date.fromisoformat(input()))
mindate = min(listDate)
print(mindate.strftime('%d-%m (%Y)'))