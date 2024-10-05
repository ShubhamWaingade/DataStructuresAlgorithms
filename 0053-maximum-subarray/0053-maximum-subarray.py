class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array_sum = nums[0]
        current_sub_array_sum = 0
        
        for ind in range(len(nums)):
            current_sub_array_sum += nums[ind]
            if max_sub_array_sum < current_sub_array_sum:
                max_sub_array_sum = current_sub_array_sum
            
            if current_sub_array_sum  < 0:
                current_sub_array_sum = 0
        return max_sub_array_sum
        