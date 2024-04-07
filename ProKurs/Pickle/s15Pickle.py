import pickle



def contrSum(filename,n):
    intList = []
    with open(filename,'rb') as file:
        obj = pickle.load(file)
        if type(obj) == list:
            for i in obj:
                if type(i) == int:
                    intList.append(i)
                elif type(i) == list:
                    for ii in i:
                        intList.append(ii)
            s = min(intList) * max(intList)
            if s == n:
                return 'Контрольные суммы совпадают'
            else:
                return 'Контрольные суммы не совпадают'
        elif type(obj) == dict:
            for key,value in obj.items():
                if type(key) == int:
                    intList.append(key)
            if sum(intList) == n:
                return 'Контрольные суммы совпадают'
            else:
                return 'Контрольные суммы не совпадают'

filename = input()
n = int(input())
print(contrSum(filename,n))