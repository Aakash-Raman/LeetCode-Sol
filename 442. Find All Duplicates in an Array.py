class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        finalList = []
        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i]:
                finalList.append(nums[i])
        return finalList
