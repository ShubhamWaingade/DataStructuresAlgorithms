class Solution {
    public int findPeakElement(int[] nums){
        if(nums.length == 1){
            return 0;
        }
        int numsLen = nums.length;
        if(nums[0] > nums[1]){
            return 0;
        }
        if(nums[numsLen-1] > nums[numsLen-2]){
            return numsLen -1;
        }

        int lowerBound = 1;
        int upperBound = numsLen - 2;

        while(lowerBound <= upperBound){
            int midPoint = lowerBound + Math.floorDiv((upperBound - lowerBound), 2);
            if((midPoint == 0 || nums[midPoint-1]< nums[midPoint]) & (midPoint == numsLen -1 || nums[midPoint+1] < nums[midPoint])){
                return  midPoint;
            }
            if(midPoint == 0 || nums[midPoint-1] < nums[midPoint]){
                lowerBound = midPoint +1;
            }else{
                upperBound = midPoint -1;
            }
        }
        return -1;
    }
}