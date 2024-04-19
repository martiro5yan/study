from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

gold = []
silver = []
bronze = []
basic = []

for u in users:
    if u.plan == 'Gold':
        gold.append(u)
    elif u.plan == 'Silver':
        silver.append(u)
    elif u.plan == 'Bronze':
        bronze.append(u)
    elif u.plan == 'Basic':
        basic.append(u)

sorted_gold = sorted(gold, key=lambda x: x[2])
sorted_silver = sorted(silver, key=lambda x: x[2])
sorted_bronze = sorted(bronze, key=lambda x: x[2])
sorted_basic = sorted(basic, key=lambda x: x[2])

result = sorted_gold+sorted_silver+sorted_bronze+sorted_basic

for i in result:
    print(i.name,i.surname)
    print(f'  Email: {i.email}')
    print(f'  Plan: {i.plan}')
    print()