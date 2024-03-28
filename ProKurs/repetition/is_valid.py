def is_valid(string):
    if 4 <= len(string) <= 6:
         return string.isdigit()
    else:
         return False


print(is_valid(input()))