def index_of_nearest(numbers,number):
    x = 0
    for n in numbers:
        if n == number:
            return numbers.index(n)
        elif n == number-x or n == number+x:
            ind = numbers.index(n)
            if type(ind) == None:
                x +=1 
                continue
            else:
                return ind



print(index_of_nearest([7, 13, 3, 5, 18], 3))