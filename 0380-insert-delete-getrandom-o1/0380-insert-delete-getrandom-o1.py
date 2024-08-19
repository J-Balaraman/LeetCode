import random

class RandomizedSet:
    def __init__(self):
        self.data_list = []
        pass

    def insert(self, val: int) -> bool:
        if val in self.data_list:
            print('false')
            return False
        self.data_list.insert(0, val)
        print('true')
        return True
            

    def remove(self, val: int) -> bool:
        if val in self.data_list:
            self.data_list.remove(val)
            print('true')
            return True
        print('false')
        return False

    def getRandom(self) -> int:
        num = random.randint(0, (len(self.data_list) - 1))
        return(self.data_list[num])
