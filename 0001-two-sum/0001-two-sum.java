class Solution {
//     public int[] twoSum(int[] nums, int target) {
        
//     }
    
    public int[] twoSum(int[] nums, int target){
        int[] twoNumbers = new int[2];
        HashMap<Integer, Integer> mapIndex = new HashMap<Integer, Integer>();

        for(int ind=0; ind<nums.length;ind++){
            int tempVal = target - nums[ind];
            if (mapIndex.getOrDefault(tempVal, -1) != -1){
                twoNumbers[0] = ind;
                twoNumbers[1] = mapIndex.get(target-nums[ind]);
                return twoNumbers;
            }else{
                mapIndex.put(nums[ind], mapIndex.getOrDefault(nums[ind], ind));
            }
        }
        return twoNumbers;
    }
}