class Solution {
        public void nextPermutation(int[] nums){
        int leftPointer = 0;
        int rightPointer = nums.length -1;
        int pivotElement = 0;
        int pivotIndex = 0;

        for (int index = nums.length-1; index > -1; index--) {
            if (index == 0){
                Arrays.sort(nums);
                return;
            } else if (nums[index-1] < nums[index]) {
                pivotIndex = index - 1;
                leftPointer = index;
                pivotElement = nums[index-1];
                break;
            }
        }

        for (int ind = nums.length-1; ind > -1; ind--) {
            if (nums[ind] > pivotElement){
                swap(nums, ind, pivotIndex);
                break;
            }
        }

        while(leftPointer < rightPointer){
            swap(nums, leftPointer, rightPointer);
            leftPointer ++;
            rightPointer --;
        }

    }

    public void swap(int[] array, int index1, int index2){
        int tempInt = array[index1];
        array[index1] = array[index2];
        array[index2] = tempInt;
    }
}