from functools import singledispatchmethod

class IPAddress:
    def __init__(self, ipaddress=None):
        if ipaddress:
            self.main(ipaddress)

    @singledispatchmethod
    def main(self, ipaddress):
        self.ipaddress = ipaddress

    @main.register(tuple)
    def tuple_main(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    @main.register(list)
    def list_main(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return f"{self.ipaddress}"
    
    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"