class Solution {
    public int trap(int[] height){
        int tempWater = 0;
        int totalWater = 0;
        int leftPointer = 0;
        int rightPointer = height.length-1;
        int leftMax = height[0];
        int rightMax = height[rightPointer];

        while (leftPointer < rightPointer){
            if (leftMax < rightMax){
                leftPointer ++;
                tempWater = leftMax - height[leftPointer];
                leftMax = Math.max(leftMax, height[leftPointer]);
            }else{
                rightPointer --;
                tempWater = rightMax - height[rightPointer];
                rightMax = Math.max(rightMax, height[rightPointer]);
            }

            if(tempWater > 0){
                totalWater += tempWater;
            }
        }
        return totalWater;
    }
}