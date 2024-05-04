

def power(degree):
    def exponentiation(x):
        return x**degree
    return exponentiation

square = power(2)
print(square(5))