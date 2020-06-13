import random as ra

class RandomizedSet:
    def __init__(self):
        self.indexes, self.list  = {}, []

    def insert(self, val: int) -> bool:
        if val in self.indexes: return False
        else:
            self.indexes[val] = len(self.list)
            self.list.append(val)
        return True
            
    def remove(self, val: int) -> bool:
        if val in self.indexes:
            pos = self.indexes[val] 
            self.list.pop(pos)
            del self.indexes[val]
            for i in range(pos, len(self.list)):
                self.indexes[self.list[i]] = i
            return True
        return False
            

    def getRandom(self) -> int:
        i = ra.randint(0, len(self.list)-1)
        return self.list[i]
