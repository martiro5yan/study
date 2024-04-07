import pickle

def filter_dump(filename, objects,typename):
    obj = []

    for i in objects:
        if type(i) == typename:
            obj.append(i)

    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
