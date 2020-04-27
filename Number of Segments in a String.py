class Solution:
    def countSegments(self, s: str) -> int:
        ctr = 0
        for i in range(0,len(s)):
            if((i == 0 or s[i-1] == ' ') and s[i] != ' '):
                ctr += 1
        return ctr
