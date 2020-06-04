class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s1 = []
        i = len(s)-1
        print(i)
        while(i >= 0):
            s1.append(s[i])
            i -= 1
        for j in range(0,len(s)):
            s[j] = s1[j]
        
        
