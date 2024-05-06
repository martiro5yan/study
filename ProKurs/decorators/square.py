import functools

def square(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        value = fun(*args,**kwargs)
        return value**2
    return wrapper


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)