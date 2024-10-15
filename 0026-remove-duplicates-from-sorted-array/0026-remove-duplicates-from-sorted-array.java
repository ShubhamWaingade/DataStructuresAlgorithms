class Solution {
    public int removeDuplicates(int[] nums) {
        int insertIndex = 1;
        for(int ind=1; ind < nums.length; ind++){
            if(nums[ind-1] != nums[ind]){
                nums[insertIndex] = nums[ind];
                insertIndex ++;
            }
        }
        return insertIndex;
    }
}