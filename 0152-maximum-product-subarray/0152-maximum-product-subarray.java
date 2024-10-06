class Solution {
    public int maxProduct(int[] nums){
        int maxProd = nums[0];
        int maxSubArrayProd = nums[0];
        int minSubArrayProd = nums[0];

        for (int ind = 1; ind < nums.length; ind++) {
            int currentMin = minSubArrayProd * nums[ind];
            int currentMax = maxSubArrayProd * nums[ind];

            maxSubArrayProd = Math.max(Math.max(currentMax, currentMin), nums[ind]);
            minSubArrayProd = Math.min(Math.min(currentMax, currentMin), nums[ind]);

            maxProd = Math.max(maxProd, maxSubArrayProd);

        }
        return  maxProd;

    }
}