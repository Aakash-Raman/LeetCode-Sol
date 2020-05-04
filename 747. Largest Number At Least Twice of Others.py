class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            f = 0
            for j in range(0, len(nums)):
                if(nums[j] != nums[i]):
                    if(nums[i] >= 2*nums[j]):
                        f += 1
            if(f == len(nums)-1):
                return i
        return -1
