import functools

def trace(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        
        v = fun(*args, **kwargs)
        if type(v) == str:
            v = f"'{v}'"
        
        krtj = tuple(args)

        dic = dict(kwargs)
        result = f"TRACE: вызов {fun.__name__}() с аргументами: {krtj}, {dic}\nTRACE: возвращаемое значение {fun.__name__}(): {v}"
        print(result)
        return fun(*args, **kwargs)
    return wrapper


@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek())    
print(beegeek.__name__)
print(beegeek.__doc__)