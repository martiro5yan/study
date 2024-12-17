



class PhoneNumber:
    def __init__(self,phone_number):
        if len(phone_number) == 10:
            self.repr_phone_number_phone_number = phone_number
            self.str_phone_number = self.create_str(phone_number)
        else:
            self.repr_phone_number = self.phone_to_string(phone_number)
            self.str_phone_number = self.phone_to_string(phone_number)
            self.str_phone_number = self.create_repr(phone_number)

    def phone_to_string(self,number):
        return number.replace(" ", "")

    def create_str(self,number):
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
    def __str__(self):
        return f"{self.str_phone_number}"

    def __repr__(self):
        return f"PhoneNumber('{self.repr_phone_number}')"
phone = PhoneNumber('9173963385')

print(str(phone))
print(repr(phone))