

class Postman:
    def __init__(self) -> None:
        self.delivery_data = []# Cписок адресов
        self.result = []

        self.street = 0
        self.home = 1
        self.flat = 2

    def add_delivery(self,street, home,flat):
        self.delivery_data.append((street,home,flat))

    def get_houses_for_street(self,street):
        del self.result[:]
        for address in self.delivery_data:
            if address[self.street] == street:
                self.result.append(address[self.home])
        self.result = list(dict.fromkeys(self.result)) 
        return self.result

    def get_flats_for_house(self,street,home):
        del self.result[:]
        for address in self.delivery_data:
            if address[self.street] == street and address[self.home] == home:
                self.result.append(address[self.flat])
        self.result = list(dict.fromkeys(self.result)) 
        return self.result       





