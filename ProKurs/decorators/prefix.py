import functools



def prefix(string,to_the_end=False):
    def dec(fun):
        @functools.wraps(fun)
        def wrapper(*args,**kwargs):
            value = fun(*args,**kwargs)
            if to_the_end == False:
                return string+value
            else:
                return value+string
        return wrapper
    return dec







@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
       
print(get_bonus())