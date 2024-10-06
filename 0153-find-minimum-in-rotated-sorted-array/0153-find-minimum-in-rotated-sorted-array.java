class Solution {
        public int findMin(int[] nums) {
            int leftPointer = 0;
            int rightPointer = nums.length-1;

            while (leftPointer < rightPointer){
                int midPoint = leftPointer + Math.floorDiv((rightPointer - leftPointer), 2);
                if(nums[midPoint] > nums[rightPointer]){
                    leftPointer = midPoint + 1;
                }else{
                    rightPointer = midPoint;
                }
            }
            return nums[leftPointer];

    }

}