def convert(string):
    characters = list(string)
    low = []
    up = []
    for c in characters:
        if c.isalpha():
            if c == c.lower():
                low.append(c)
            elif c  == c.upper():
                up.append(c)
    if len(up) > len(low):
        return string.upper()
    else:
        return string.lower()


print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('PI31415!'))