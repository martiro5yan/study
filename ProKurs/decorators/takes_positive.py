




def takes_positive(fun):
    def dec(*args,**kwargs):
        try:
            for n in args:
                if type(n) != int:
                    raise TypeError
                elif n <= 0:
                    raise ValueError
            

            for n in kwargs.values():
                #print(n)
                if type(n) != int:
                    raise TypeError
                elif n <= 0:
                    raise ValueError              
            return fun(*args,**kwargs)
        except (TypeError,ValueError) as err:
            return type(err)
    return dec


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))