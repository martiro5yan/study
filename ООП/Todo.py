
class Todo:
    def __init__(self):
        self.things = []
        self.result = []
    # Медот принимающий название и приоритет дела
    # добовляющий в список в виде кортежа
    def add(self,case,priority):
        self.task_tuple = (case,priority)
        self.things.append(self.task_tuple)
    # Метод вызывающий список дел имеющий приоритет n
    def get_by_priority(self,n):
        del self.result [:]
        priority = n
        for case in self.things:
            if case[1] == priority:
                self.result.append(case[0])
        return self.result
    # Метод вызывающий cписок дел с минимальным приоритетом 
    def get_low_priority(self):
        del self.result [:]
        if len(self.things) == 0:
            return self.things
        else:
            low_priority = min(self.things, key=lambda x: x[1]) 
            for case in self.things:
                if case[1] == low_priority[1]:
                    self.result.append(case[0])
            return self.result
    # Метод вызывающий список дел с макс приоритетом
    def get_high_priority(self):
        del self.result [:]
        if len(self.things) == 0:
            return self.things
        else:
            max_priority = max(self.things, key=lambda x: x[1]) 
            for case in self.things:
                if case[1] == max_priority[1]:
                    self.result.append(case[0])
            return self.result
