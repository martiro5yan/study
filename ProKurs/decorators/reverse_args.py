

def reverse_args(func):
    def wrapper(*args,**kwargs):
        args = args[::-1]
        return func(*args,**kwargs)
    return wrapper



@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))