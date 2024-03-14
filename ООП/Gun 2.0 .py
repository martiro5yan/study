
class Gun:
    def __init__(self):
        self.count = 0

    def shots_reset(self):
        self.count = 0

    def shoot(self):
        self.count += 1
        if self.count % 2 == 0:
            print("paf")
        else:
            print('pif')

    def shots_count(self):
        return self.count

gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())