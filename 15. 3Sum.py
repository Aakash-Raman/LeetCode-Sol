class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        if(nums == null || nums.length == 0) return new ArrayList<>();
       
        Set<Pair> set = new HashSet<>();
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 2; i++){
            int j = i + 1, k = nums.length - 1;
            int target = -nums[i];
            while(j < k){
                if(nums[j] + nums[k] == target){
                    if(!set.contains(new Pair(nums[i], nums[k]))){
                        res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                        set.add(new Pair(nums[i], nums[k]));
                    }
                    j++;
                    k--;
                }
                else if(nums[j] + nums[k] > target) k--;
                else j++;  
            }
        }
        return res;
    }
}
