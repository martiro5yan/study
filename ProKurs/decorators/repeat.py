import functools

def repeat(times):
    def dec(fun):
        @functools.wraps(fun)
        def wrapper(*args,**kwargs):
            
            for _ in range(times):
                result = fun(*args,**kwargs)
            return result
        return wrapper
    return dec

@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
say_beegeek()

@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b
    
print(add.__name__)
print(add.__doc__)
print(add(10, b=20))
