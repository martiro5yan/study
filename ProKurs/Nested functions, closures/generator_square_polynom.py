def generator_square_polynom(a,b,c):
    def the_quadratic_function(x):
        result = a*x**2+(b*x) + c
        return result
    return the_quadratic_function



print(generator_square_polynom(9, 52, 64)(8))