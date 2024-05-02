

def triangle(h):
    if h != 0:
        print('*'*h)
        triangle(h-1)
        # step 10
        # triangle(h-1)
        # print('*'*h)

triangle(3)