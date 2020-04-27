class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ctr = 0
        l = 0
        for i in s:
            if(i == 'R'):
                ctr += 1
            if(i == 'L'):
                ctr -= 1
            if(ctr == 0):
                l += 1
        return l
