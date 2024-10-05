class Solution {
        public int[] productExceptSelf(int[] nums) {
        int arrayLen = nums.length;
        int[] ans_array = new int[arrayLen];
        Arrays.fill(ans_array, 1);

        int prefixValue = 1;
        int postfixValue = 1;

        for (int ind = 0; ind < arrayLen; ind++) {
            ans_array[ind] = prefixValue;
            prefixValue *= nums[ind];
        }

        for (int postInd = arrayLen-1; postInd > -1; postInd--) {
            ans_array[postInd] = ans_array[postInd] * postfixValue;
            postfixValue = nums[postInd] * postfixValue;
        }

        return ans_array;
    }
}