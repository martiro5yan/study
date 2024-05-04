


def exception_decorator(fun):
    def dec(*args,**kwargs):
        try:
            result = fun(*args,**kwargs)
            return (result,'Функция выполнилась без ошибок')
        except:
            return (None,'При вызове функции произошла ошибка')
    return dec


sum = exception_decorator(sum)

print(sum(['199', '1', 187]))