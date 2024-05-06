import functools

def returns_string(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        v = fun(*args,**kwargs)
        if type(v) != str:
            raise TypeError
        return v
    return wrapper
#TEST 4
@returns_string
def nothing():
    return

print(nothing.__name__)
print(nothing.__doc__)

try:
    nothing()
except TypeError as e:
    print(type(e))