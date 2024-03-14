
class Scales:
    def __init__(self,left_bowl=0, right_bowl=0):
        self.left_bowl = left_bowl
        self.right_bowl = right_bowl
        
    def add_right(self,m):
        self.right_bowl += m

    def add_left(self,m):
        self.left_bowl += m
    
    def get_result(self):
        if self.right_bowl == self.left_bowl:
            return 'Весы в равновесии'
        elif self.left_bowl > self.right_bowl:
            return 'Левая чаша тяжелее'
        else:
            return 'Правая чаша тяжелее'