from itertools import permutations as perm
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(list(map(str, list(perm(list(range(1,n+1))))[k-1])))
