from datetime import date
listDate = []
for _ in range(int(input())):
    listDate.append(date.fromisoformat(input()))

listDate.sort(reverse=True)

for i in listDate:
    print(i.strftime('%d/%m/%Y'))
