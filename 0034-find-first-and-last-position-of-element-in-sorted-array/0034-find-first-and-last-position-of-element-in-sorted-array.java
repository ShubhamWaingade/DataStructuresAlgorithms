class Solution {
    public int[] searchRange(int[] nums, int target){
        int firstIndex = findBound(nums, target, true);
        if(firstIndex == -1){
            return IntStream.of(-1, -1).toArray();
        }
        int secondIndex = findBound(nums, target, false);
        return IntStream.of(firstIndex, secondIndex).toArray();

    }

    public int findBound(int[] nums, int target, boolean isFirst){
        int leftPointer = 0;
        int rightPointer = nums.length-1;

        while(leftPointer <= rightPointer){
            int midPoint = leftPointer + Math.floorDiv((rightPointer-leftPointer), 2);
            if(nums[midPoint] == target){
                if(isFirst){
                    if(midPoint==leftPointer || nums[midPoint-1] != target){
                        return midPoint;
                    }
                    rightPointer = midPoint-1;
                }else {
                    if(midPoint == rightPointer || nums[midPoint+1] != target){
                        return midPoint;
                    }
                    leftPointer = midPoint + 1;
                }
            } else if (nums[midPoint] > target) {
                rightPointer = midPoint -1;
            }else {
                leftPointer = midPoint + 1;
            }
        }
        return -1;
    }
}