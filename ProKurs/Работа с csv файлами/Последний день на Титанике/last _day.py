import csv

with open('titanic.csv', 'r', encoding='UTF-8') as file:
    passenger_list = csv.reader(file, delimiter=';')
    next(passenger_list)
    male_list = []
    female_list = []
    for name in passenger_list:
        #print(name)
        if int(name[0]) == 1 and float(name[3]) < 18 and name[2] == 'male':
            male_list.append(name[1])
        elif int(name[0]) == 1 and float(name[3]) < 18 and name[2] == 'female':
            female_list.append(name[1])
    
    result = male_list+female_list

    for i in result:
        print(i)
        
    