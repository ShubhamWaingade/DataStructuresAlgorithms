class Solution {
    public int search(int[] nums, int target){
        int leftPointer = 0;
        int rightPointer = nums.length-1;
        
        
        
        while(leftPointer <= rightPointer){
            int midPoint = leftPointer + Math.floorDiv((rightPointer - leftPointer), 2);
            if (nums[midPoint] == target){
                return midPoint;
            }
            if(nums[leftPointer] <= nums[midPoint]){
                if(target < nums[leftPointer] || nums[midPoint] < target){
                    leftPointer = midPoint + 1;
                }else{
                    rightPointer = midPoint - 1;
                }
            }
            else{
                if(nums[rightPointer] < target || target < nums[midPoint]){
                    rightPointer = midPoint  - 1;
                }else{
                    leftPointer = midPoint + 1;
                }
            }
        }

        return -1;        
        }
    }
