class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newlist = []
        for i in range(0,len(nums)):
            ctr = 0
            for j in range(0,len(nums)):
                if(nums[j] < nums[i]):
                    ctr += 1
            newlist.append(ctr)        
        
        return newlist
