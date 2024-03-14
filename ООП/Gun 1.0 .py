
# Работает 
class Gun:
    def __init__(self):
        self.count = 0
    def shoot(self):
        self.count += 1
        if self.count % 2 == 0:
            print("paf")
        else:
            print('pif')

# не работает
# class Gun:
#     def shoot(self):
#         count = 0
#         count += 1
#         if count % 2 == 0:
#             print("paf")
#         else:
#             print('pif')

gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()