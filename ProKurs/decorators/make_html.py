import functools


def make_html(tag):
    def dec(fun):
        @functools.wraps(fun)
        def wrapper(*args,**kwargs):
            s = fun(*args,**kwargs)
            return f'<{tag}>{s}</{tag}>'
        return wrapper
    return dec




@make_html('i')
@make_html('del')
def get_text(text):
    return text
    
print(get_text(text='decorators are so cool!'))