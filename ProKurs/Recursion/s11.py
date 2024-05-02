
def rec(n, r, o, p=''):
    if n == 4:
        print(p * o, n * r)
    else:
        print(p * o, n * r)
        p = ' '
        rec(n + 1, r - 4, o + 2, p)
        print(p * o, n * r)

rec(1, 16, 0)
