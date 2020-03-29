class Solution {
    public int singleNumber(int[] nums) {
     int ctr,i,j;
     int n=nums.length;
        for(i=0;i<n;i++)
        {
            ctr=0;
            for(j=0;j<n;j++)
            {
                if(nums[i]==nums[j])
                {
                    ctr+=1;
                }
            }
            if(ctr==1)
                    return nums[i];
        }
        return 1;
    }
}
