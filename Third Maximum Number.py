class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n_set=set(nums)
        new_list=list(n_set)
        new_list.sort()
        set_len=len(new_list)
        if(set_len==1):
            return new_list[0]
        elif(set_len==2):
            if(new_list[0]>new_list[1]):
                return new_list[0]
            else:
                return new_list[1]
        else:
            return new_list[set_len-3]
        
            
