import random

class RandomizedSet:
    def __init__(self):
        self.data_list = []
        pass

    def insert(self, val: int) -> bool:
        if val in self.data_list:
            return False
        self.data_list.insert(0, val)
        return True
            

    def remove(self, val: int) -> bool:
        if val in self.data_list:
            self.data_list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        num = random.randint(0, (len(self.data_list) - 1))
        return(self.data_list[num])
