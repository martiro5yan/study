number_list = []
class Numbers:
    
    def add_number(self,n):
        number_list.append(n)

    def get_even(self):
        list_even_numbers = []
        for n in number_list:
            if n % 2 == 0:
                list_even_numbers.append(n)
        return list_even_numbers
    
    def get_odd(self):
        list_odd_numbers = []
        for n in number_list:
            if n % 2 != 0:
                list_odd_numbers.append(n)
        return list_odd_numbers
numbers = Numbers()

#Test 5 
numbers.add_number(1)
numbers.add_number(2)
numbers.add_number(3)
numbers.add_number(4)

even = numbers.get_even()
odd = numbers.get_odd()
print(numbers.get_even())
print(numbers.get_odd())

even.append(None)
odd.append(None)
print(numbers.get_even())


print(numbers.get_odd())



# # TEST_5:
# [2, 4]
# [1, 3]
# [2, 4]
# [1, 3]