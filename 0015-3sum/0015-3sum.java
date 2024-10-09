class Solution {
    public List<List<Integer>> threeSum(int[] nums){
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for (int ind = 0; ind < nums.length && nums[ind] <= 0; ind++) {
            if(ind == 0 || nums[ind] != nums[ind-1]){
                intTwoSum(nums, ind, result);
            }
        }
        return  result;
    }

    void intTwoSum(int[] nums, int ind, List<List<Integer>> result){
        int leftPointer = ind + 1;
        int rightPointer = nums.length - 1;

        while(leftPointer < rightPointer) {
            int sum = nums[ind] + nums[leftPointer] + nums[rightPointer];
            if(sum < 0){
                leftPointer ++;
            } else if (sum > 0) {
                rightPointer --;
            }else{
                result.add(Arrays.asList(nums[ind], nums[leftPointer++], nums[rightPointer--]));
                while(leftPointer < rightPointer && nums[leftPointer] == nums[leftPointer-1]){
                    leftPointer ++;
                }
            }
        }
    }
}