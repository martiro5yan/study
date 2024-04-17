from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])


with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)

    for t in obj:
        print(f'name: {t.name}')
        print(f'family: {t.family}')
        print(f'sex: {t.sex}')
        print(f'color: {t.color}')
        print()