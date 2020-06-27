class Solution:
    def numSquares(self, n: int) -> int:
        nums = set()
        
        if n == 0:
            return 0 #Base case
        
        #Find all the Squares les than equal to n
        
        for i in range(n+1):
            if i**2 <= n:
                nums.add(i**2)
                if i**2 == n : #if N is perfect square
                    return 1
            else:
                break
                
        res = 4 #N can be represented by maximun 4 numbers 
        
        #check for 2 and 3 using 2sum and 3sum problem  
        
        for i in nums:
            
            if (n-i) in nums:
                res = min(res,2) #check for 2 Sum problem
                return res           # min is 2
            for j in nums :
                
                if (n-i-j) in nums :
                    
                    res = min(res,3) #check for 3 Sum problem
        
        return res
