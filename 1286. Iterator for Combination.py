class CombinationIterator:
    def __init__(self, characters: str, l: int):
        self.comb = list(itertools.combinations(characters ,l))  
        self.index = 0    
        self.length = len(self.comb)  

    def next(self) -> str:
        self.index += 1 
        return ''.join(self.comb[self.index-1]) 

    def hasNext(self) -> bool:
        return self.index < self.length  
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
