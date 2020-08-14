class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = {}
        for i in s:
            if i not in letter:
                letter[i]=1
            else:
                letter[i]+=1
        res = 0
        count = 0
        if len(letter) == 1:
            return letter[s[0]]
        
        for i in letter.values():
            if i > 1:
                if i % 2 == 0:
                    res += i
                else:
                    res += i - 1
                    count += 1
            else:
                count += 1       
        if count > 0:
            res += 1
        return res
