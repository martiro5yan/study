class AnyClass:
    def __init__(self, **kwargs):
        self.add_attributes(**kwargs)

    def add_attributes(self, **kwargs):
        for attribut, value in kwargs.items():
            self.__dict__[attribut] = value

    def __str__(self):
        # Формирование строкового представления объекта без фигурных скобок
        value = ', '.join(f"{key}={repr(value)}" for key, value in self.__dict__.items())
        return f"AnyClass: {value}"

    def __repr__(self):
        # Использование __str__ для получения единого представления
        return f"AnyClass({', '.join(f'{key}={repr(value)}' for key, value in self.__dict__.items())})"

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))