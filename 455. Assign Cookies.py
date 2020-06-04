class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        #Time: O(nlogn)
        #Space O(1)
        happy=0
        g.sort()
        s.sort() 
        child,cookie=0,0
        while child <len(g) and cookie<len(s):
            
            if g[child]<=s[cookie]:
                
                happy+=1
                child+=1
            cookie+=1
        return happy
