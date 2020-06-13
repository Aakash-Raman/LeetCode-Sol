def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    
    if not nums:
        return []
    
    n = len(nums)
    nums.sort()
    dp = [1 for i in range(n)]
    
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i],dp[j]+1)
                
    m = max(dp)
    val = 1
    
    res = []
    i = 0
    while val <= m and i < n:
        if dp[i] == val:
            res.append(nums[i])
            val+=1
        i+=1
    
    return res
